from functions import *


def main():
    municipios = get_municipios()
    # print(len(municipios))
    num_threads = 100
    batch_size = 250
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        for i in range(0, len(municipios), batch_size):
            municipios_lote = municipios[i:i + batch_size]
            executor.submit(process_municipios_lote, municipios_lote)

    print("Script finalizado")

if __name__ == "__main__":
    main()
