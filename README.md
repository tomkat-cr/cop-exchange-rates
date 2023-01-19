# cop-exchange-rates

## English

API to get Colombian Pesos currency exchange rates with Python.<br/>
Includes daily currency exchange rates of US Dollar from official government API ([datos.gov.co](https://www.datos.gov.co/)) and other sources like Google Finance ([google.com/finance](https://www.google.com/finance/quote/USD-COP)).

## Production API call

[https://cop-exchange-rates.vercel.app/get_exchange_rates](https://cop-exchange-rates.vercel.app/get_exchange_rates)

```json
{
  "error": false,
  "error_message": [],
  "data": {
    "official_cop": {
      "error": false,
      "error_message": "",
      "data": {
        "valor": "4702.67",
        "unidad": "COP",
        "vigenciadesde": "2023-01-19T00:00:00.000",
        "vigenciahasta": "2023-01-19T00:00:00.000",
        ":id": "row-bebx~s2c5-95zv",
        "bank_value": "4727.59"
      },
      "run_timestamp":"2023-01-19 02:56:57 UTC"
    },
    "google_cop": {
      {
        "error": false,
        "error_message": "",
        "data": {
          "unit": "USD / COP",
          "value": "4703.4800",
          "bank_value": "4750.51",
          "effective_date": "Jan 19, 12:26:00 AM UTC"
        },
        "run_timestamp":"2023-01-19 02:56:57 UTC"
      }
    },
  }
}
```

[https://cop-exchange-rates.vercel.app/get_google_cop](https://cop-exchange-rates.vercel.app/get_google_cop)

```json
{
  "error": false,
  "error_message": "",
  "data": {
    "unit": "USD / COP",
    "value": "4703.4800",
    "bank_value": "4750.51",
    "effective_date": "Jan 19, 12:26:00 AM UTC"
  },
  "run_timestamp":"2023-01-19 02:56:57 UTC"
}
```

[https://cop-exchange-rates.vercel.app/get_official_cop](https://cop-exchange-rates.vercel.app/get_official_cop)

```json
{
  "error": false,
  "error_message": "",
  "data": {
      "valor": "4702.67",
      "unidad": "COP",
      "vigenciadesde": "2023-01-19T00:00:00.000",
      "vigenciahasta": "2023-01-19T00:00:00.000",
      ":id": "row-bebx~s2c5-95zv",
      "bank_value": "4727.59"
  },
  "run_timestamp": "2023-01-19 03:00:12 UTC"
}
```

* NOTE: `bank_value` is the approximate value offered on international wire transfers.

## What is an API?

APIs are mechanisms that allow two software components or programs to communicate with each other using a set of definitions and protocols. For example, this cop-exchange-rates API returns daily exchange rate data taken from the BCV website. An application on your phone that needs to do currency conversion "talks" to this system through the APIs and shows you daily exchange updates for dollar, euro, yen, ruble, yuan, and lira on your phone.

## What does API mean?

API stands for "Application Programming Interface". In the context of APIs, the word "application" refers to any software or program with distinct and/or independent functions. The interface can be thought of as a service contract between two applications. This contract defines how they communicate with each other through requests and responses. Your API documentation should contain information about how developers should structure those requests and responses.

<br/>

------------------------------

## Spanish

API de contización del dolar respecto al Peso Colombiano en Python.<br/>
Incluye actualizaciones de cambio monetarias diarias del dólar de fuentes oficiales de Colombia ([datos.gov.co](https://www.datos.gov.co/)) y otras fuentes como Google Finance ([google.com/finance](https://www.google.com/finance/quote/USD-COP)).

## Llamada a la API de producción

[https://cop-exchange-rates.vercel.app/get_exchange_rates](https://cop-exchange-rates.vercel.app/get_exchange_rates)

```json
{
  "error": false,
  "error_message": [],
  "data": {
    "official_cop": {
      "error": false,
      "error_message": "",
      "data": {
        "valor": "4691.09",
        "unidad": "COP",
        "vigenciadesde": "2023-01-18T00:00:00.000",
        "vigenciahasta": "2023-01-18T00:00:00.000",
        ":id": "row-bebx~s2c5-95zv"
      },
      "run_timestamp":"2023-01-19 02:56:57 UTC"
    },
    "google_cop": {
      {
        "error": false,
        "error_message": "",
        "data": {
          "unit": "USD / COP",
          "value": "4703.4800",
          "effective_date": "Jan 19, 12:26:00 AM UTC"
        },
        "run_timestamp":"2023-01-19 02:56:57 UTC"
      }
    },
  }
}
```

[https://cop-exchange-rates.vercel.app/get_google_cop](https://cop-exchange-rates.vercel.app/get_google_cop)

```json
{
  "error": false,
  "error_message": "",
  "data": {
    "unit": "USD / COP",
    "value": "4703.4800",
    "effective_date": "Jan 19, 12:26:00 AM UTC"
  },
  "run_timestamp":"2023-01-19 02:56:57 UTC"
}
```

[https://cop-exchange-rates.vercel.app/get_official_cop](https://cop-exchange-rates.vercel.app/get_official_cop)

```json
{
  "error": false,
  "error_message": "",
  "data": {
      "valor": "4702.67",
      "unidad": "COP",
      "vigenciadesde": "2023-01-19T00:00:00.000",
      "vigenciahasta": "2023-01-19T00:00:00.000",
      ":id": "row-gfv7-yqt5-kppv"
  },
  "run_timestamp": "2023-01-19 03:00:12 UTC"
}
```

* NOTA: `bank_value` es el valor aproximado ofrecido en las transferencias internacionales.

## ¿Qué es una API?

Las API son mecanismos que permiten a dos componentes de software o programas comunicarse entre sí mediante un conjunto de definiciones y protocolos. Por ejemplo, esta API cop-exchange-rates devuelve datos de tasas de cambios diarias tomadas del sitio web del BCV. Una aplicación de su teléfono que necesite hacer conversión monetaria "habla" con este sistema a través de las API y le muestra en su teléfono las actualizaciones del cambio diarias de dólares, euros, yenes, rublos, yuanes y liras.

## ¿Qué significa API?

API son las siglas de "interfaz de programación de aplicaciones". En el contexto de las API, la palabra aplicación se refiere a cualquier software o programa con funciones distintas y/o independientes. La interfaz puede considerarse como un contrato de servicio entre dos aplicaciones. Este contrato define cómo se comunican entre sí mediante solicitudes y respuestas. La documentación de su API debe contener información sobre cómo los desarrolladores deben estructurar esas solicitudes y respuestas.
