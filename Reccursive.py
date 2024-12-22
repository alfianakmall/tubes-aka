def analyze_wait_time_recursive(arrival_times, service_times, i=0, wait_times=None, end_service_times=None):
    if wait_times is None:
        wait_times = [0] * len(arrival_times)
    if end_service_times is None:
        end_service_times = [0] * len(arrival_times)

    # Base case: Jika sudah menghitung semua pelanggan
    if i == len(arrival_times):
        return wait_times, end_service_times

    # Menghitung waktu tunggu dan selesai layanan untuk pelanggan saat ini
    if i == 0:
        wait_times[i] = 0  # Pelanggan pertama tidak menunggu
    else:
        wait_times[i] = max(0, end_service_times[i - 1] - arrival_times[i])
    
    end_service_times[i] = arrival_times[i] + wait_times[i] + service_times[i]

    # Rekursi untuk pelanggan berikutnya
    return analyze_wait_time_recursive(arrival_times, service_times, i + 1, wait_times, end_service_times)

# Contoh penggunaan
arrival_times = [1, 3, 5, 7]  # Waktu kedatangan pelanggan
service_times = [2, 3, 1, 2]  # Durasi layanan untuk masing-masing pelanggan
wait_times, end_service_times = analyze_wait_time_recursive(arrival_times, service_times)

# Menampilkan hasil
for i in range(len(arrival_times)):
    print(f"Pelanggan ke-{i + 1}: Waktu tunggu = {wait_times[i]}, Waktu selesai layanan = {end_service_times[i]}")
