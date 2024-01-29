#include <WiFi.h>
#include <HTTPClient.h>

const char *ssid = "TECNICO";
const char *password = "DTC.2020";
const char *apiUrl = "http://chatbot-ojievlbbua-uc.a.run.app/";

void setup() {
  Serial.begin(115200);

  // Conectar a WiFi
  WiFi.begin(ssid, password);

  Serial.print("Conectando");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("Conexión exitosa!");
  Serial.print("Dirección IP asignada: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    // Crear una instancia de la clase HTTPClient
    HTTPClient http;

    // Hacer la petición GET a la API
    http.begin(apiUrl);

    int httpCode = http.GET();
    if (httpCode > 0) {
      // Si la respuesta fue exitosa, imprimir el contenido de la respuesta
      String payload = http.getString();
      Serial.println("Respuesta de la API:");
      Serial.println(payload);
    } else {
      Serial.print("Error en la petición HTTP, código de error: ");
      Serial.println(httpCode);
    }

    // Liberar los recursos
    http.end();
  }

  // Esperar antes de hacer la siguiente petición
  delay(5000);  // Esperar 5 segundos antes de la siguiente petición
}
