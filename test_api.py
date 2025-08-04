import requests

# Configuración de la API
APIKEY = "1d5b57a92e0a42a69d944cdf68b86d12"
API_BASE_URL = "http://23.175.40.59:8585/back/api/v2/informe"

def test_api():
    """Probar si la API está funcionando"""
    print("🔍 Probando conexión a la API...")
    
    # Probar conexión básica
    try:
        response = requests.get(f"{API_BASE_URL}/dni/12345678?apikey={APIKEY}", timeout=10)
        print(f"✅ Conexión exitosa - Status: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ La API está funcionando correctamente")
            return True
        elif response.status_code == 404:
            print("✅ La API responde (404 es normal para DNI inexistente)")
            return True
        else:
            print(f"⚠️ La API responde pero con status: {response.status_code}")
            return True
            
    except requests.exceptions.ConnectionError as e:
        print(f"❌ Error de conexión: {e}")
        print("💡 Posibles soluciones:")
        print("   • El servidor está caído")
        print("   • Necesitas VPN")
        print("   • La IP cambió")
        return False
        
    except Exception as e:
        print(f"❌ Error general: {e}")
        return False

if __name__ == "__main__":
    test_api() 