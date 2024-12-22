def analyze_wait_time_iterative(arrival_times, service_times):
    n = len(arrival_times)
    wait_times = [0] * n
    end_service_times = [0] * n

    for i in range(n):
        if i == 0:
            wait_times[i] = 0
            end_service_times[i] = arrival_times[i] + service_times[i]  # Hitung waktu selesai pelanggan pertama
        else:
            wait_times[i] = max(0, end_service_times[i - 1] - arrival_times[i])
            end_service_times[i] = arrival_times[i] + wait_times[i] + service_times[i]
    
    return wait_times, end_service_times

# Input data
arrival_times = [1, 3, 5, 7]  # Waktu kedatangan pelanggan
service_times = [2, 3, 1, 2]  # Durasi layanan untuk masing-masing pelanggan

# Analisis waktu tunggu dan selesai
wait_times, end_service_times = analyze_wait_time_iterative(arrival_times, service_times)

# Menampilkan hasil
for i in range(len(arrival_times)):
    print(f"Pelanggan ke-{i + 1}: Waktu tunggu = {wait_times[i]}, Waktu selesai layanan = {end_service_times[i]}")
