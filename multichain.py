from Savoir import Savoir

class MultiChain:
    def __init__(self, rpcuser, rpcpasswd, rpchost, rpcport, chainname):
        self.api = Savoir(rpcuser, rpcpasswd, rpchost, rpcport, chainname)

    def create_address(self):
        return self.api.getnewaddress()

    def grant_permissions(self, address, permissions):
        return self.api.grant(address, permissions)

    def create_token(self, address, token_name, quantity, units=1.0, open=True):
        return self.api.issue(address, token_name, quantity, units, {"open": open})

    def transfer(self, from_address, to_address, token, amount):
        return self.api.sendassetfrom(from_address, to_address, token, amount)

    def get_blockchain_info(self):
        return self.api.getinfo()

    def create_stream(self, name, open=True):
        return self.api.create("stream", name, open)

    def write_to_stream(self, stream_name, key, data):
        return self.api.publish(stream_name, key, data)

    def get_address_balance(self, address):
        return self.api.getaddressbalances(address)
    
    def read_from_stream(self, stream_name, key):
        return self.api.liststreamkeyitems(stream_name, key)


def main():
    # Configuración
    rpcuser = "multichainrpc"
    rpcpasswd = "3KNkrGKCFfpkRTUqg9rrPyzizyCm2Aj6VuYFvn7fVwbn"
    rpchost = "20.10.164.130"
    rpcport = "8342"
    chainname = "test1"

    # Instanciar la clase
    multichain = MultiChain(rpcuser, rpcpasswd, rpchost, rpcport, chainname)

    while True:
        print("\nSelecciona una acción:")
        print("1. Crear dirección")
        print("2. Otorgar permisos a dirección")
        print("3. Crear token")
        print("4. Transferir tokens")
        print("5. Obtener información de la blockchain")
        print("6. Crear un stream")
        print("7. Escribir en un stream")
        print("8. Obtener balance de una dirección")
        print("9. Salir")

        choice = input("Tu elección: ")

        if choice == "1":
            address = multichain.create_address()
            print(f"Nueva dirección creada: {address}")

        elif choice == "2":
            address = input("Dirección: ")
            permissions = input("Permisos (separados por coma, ej: issue,send,receive): ")
            result = multichain.grant_permissions(address, permissions)
            print(f"Permisos otorgados: {result}")

        elif choice == "3":
            address = input("Dirección para emitir el token: ")
            token_name = input("Nombre del token: ")
            quantity = float(input("Cantidad a emitir: "))
            result = multichain.create_token(address, token_name, quantity)
            print(f"Token creado con TXID: {result}")

        elif choice == "4":
            from_address = input("Dirección de origen: ")
            to_address = input("Dirección de destino: ")
            token = input("Nombre del token: ")
            amount = float(input("Cantidad a transferir: "))
            result = multichain.transfer(from_address, to_address, token, amount)
            print(f"Transferencia completada con TXID: {result}")

        elif choice == "5":
            info = multichain.get_blockchain_info()
            print(info)

        elif choice == "6":
            stream_name = input("Nombre del stream: ")
            result = multichain.create_stream(stream_name)
            print(f"Stream creado con TXID: {result}")

        elif choice == "7":
            stream_name = input("Nombre del stream: ")
            key = input("Clave: ")
            data = input("Datos (en texto): ")
            result = multichain.write_to_stream(stream_name, key, data)
            print(f"Datos escritos con TXID: {result}")

        elif choice == "8":
            address = input("Dirección: ")
            balance = multichain.get_address_balance(address)
            print(f"Balance: {balance}")

        elif choice == "9":
            stream_name = input("Nombre del stream: ")
            key = input("Clave del valor que deseas leer: ")
            items = multichain.read_from_stream(stream_name, key)
            if items:
                for item in items:
                    print(f"Datos: {item['data']}")
            else:
                print("No se encontraron datos para esa clave en el stream especificado.")


        elif choice == "10":
            break

        else:
            print("Elección no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()

