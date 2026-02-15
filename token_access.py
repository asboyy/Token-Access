# -----------------------------
# CLOUD ACCESS TOKEN DATABASE
# -----------------------------
access_tokens = {
    "TOKEN-ADMIN-123": {
        "owner": "admin",
        "role": "ADMIN",
        "status": "AKTIF"
    },
    "TOKEN-USER-456": {
        "owner": "fahmi",
        "role": "USER",
        "status": "AKTIF"
    }
}

# -----------------------------
# CLOUD DATA
# -----------------------------
cloud_data = {
    "data_gaji": ["ADMIN"],
    "profil_pribadi": ["ADMIN", "USER"]
}

# -----------------------------
# SIMULASI AKSES CLOUD
# -----------------------------
print("=== CLOUD ACCESS SYSTEM ===")
token_input = input("Masukkan access token: ")
data_request = input("Masukkan data yang ingin diakses: ")

if token_input in access_tokens:
    token_info = access_tokens[token_input]

    if token_info["status"] != "AKTIF":
        print("Token tidak aktif ❌")

    elif data_request in cloud_data:
        if token_info["role"] in cloud_data[data_request]:
            print("Akses diberikan ✅")
            print(f"Pemilik Token : {token_info['owner']}")
            print(f"Role          : {token_info['role']}")
            print(f"Data diakses  : {data_request}")
        else:
            print("Akses ditolak ❌")
            print("Hak akses tidak mencukupi")
    else:
        print("Data tidak ditemukan ❌")
else:
    print("Token tidak valid ❌")
