# cop-exchange-rates

![COP Exchange Rates](./assets/cop.echange.rates.banner.010.png)

API to get Colombian Pesos (COP) currency exchange rates.

[English](#english) | [Español](#español)

[![Version](https://img.shields.io/badge/version-1.1.1-blue.svg)](https://github.com/tomkat-cr/cop-exchange-rates)
[![Python](https://img.shields.io/badge/python-3.9%2B-brightgreen.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## English

API to get Colombian Pesos currency exchange rates with Python.<br/>
Includes daily currency exchange rates of US Dollar from official government API ([datos.gov.co](https://www.datos.gov.co/)) and other sources like Google Finance ([google.com/finance](https://www.google.com/finance/quote/USD-COP)).

## Table of Contents

- [Development Setup](#development-setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Available Commands](#available-commands)
- [Local Development](#local-development)
- [Deployment](#deployment)
- [PyPI Publishing](#pypi-publishing)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [API Response Examples](#api-response-examples)

## Development Setup

### Prerequisites

- Python 3.9 - 3.13
- Node.js (for Vercel deployment)
- Poetry (recommended) or pip

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/tomkat-cr/cop-exchange-rates.git
   cd cop-exchange-rates
   ```

2. **Set up the environment:**
   ```bash
   make update  # Clean install with all dependencies
   ```

   Or manually:
   ```bash
   make clean   # Clean previous installations
   make run     # Set up virtual environment and install dependencies
   ```

## Available Commands

The project includes a Makefile with the following commands:

### Development Commands

| Command | Description |
|---------|-------------|
| `make` or `make all` | Show this Makefile |
| `make clean` | Clean build artifacts and virtual environment |
| `make update` | Clean install - removes existing setup and reinstalls everything |
| `make run` | Set up virtual environment and run the API locally (returns JSON output) |
| `make run_module` | Run the CLI module only (same as "make run") |

### Environment Management

| Command | Description |
|---------|-------------|
| `make deactivate` | Deactivate the virtual environment |
| `make pipfile` | Update Pipfile.lock (if using pipenv) |

### Deployment Commands

| Command | Description |
|---------|-------------|
| `make run_vercel` | Run local Vercel development server on port 5001 |
| `make deploy_prod` | Deploy to Vercel production |
| `make rename_staging` | Rename staging deployment |

### PyPI Publishing Commands

| Command | Description |
|---------|-------------|
| `make pypi-build` | Build distribution packages for PyPI |
| `make pypi-publish-test` | Publish to PyPI test repository |
| `make pypi-publish` | Publish to PyPI production |

## Local Development

### Quick Start

1. **Run locally:**
   ```bash
   make run
   ```
   This will:
   - Create a virtual environment in `cop_exchange_rates/`
   - Install all dependencies
   - Run the CLI version and display JSON output

2. **Run Vercel development server:**
   ```bash
   make run_vercel
   ```
   The API will be available at `http://localhost:5001`

### Environment Variables

Create a `.env` file in the project root for any environment-specific configurations.

## Deployment

### Vercel Deployment

1. **Deploy to production:**
   ```bash
   make deploy_prod
   ```

2. **Run local Vercel development:**
   ```bash
   make run_vercel
   ```

The project is configured with `vercel.json` for automatic deployment.

## PyPI Publishing

This project can be published to PyPI as a Python package:

1. **Build the package:**
   ```bash
   make pypi-build
   ```

2. **Test publish:**
   ```bash
   make pypi-publish-test
   ```

3. **Production publish:**
   ```bash
   make pypi-publish
   ```

## Project Structure

```
cop-exchange-rates/
├── cop_exchange_rates/          # Main Python package
│   ├── __init__.py
│   ├── index.py                 # FastAPI application & CLI entry point
│   ├── cop.py                   # Core exchange rate logic
│   └── requirements.txt         # Python dependencies
├── Makefile                     # Development commands
├── run.sh                       # Shell script for various operations
├── pyproject.toml              # Poetry configuration & package metadata
├── package.json                # Node.js configuration for Vercel
├── vercel.json                 # Vercel deployment configuration
└── README.md                   # This file
```

## API Endpoints

The API provides three main endpoints:

- `GET /get_exchange_rates` - Combined rates from all sources
- `GET /get_official_cop` - Official Colombian government rates
- `GET /get_google_cop` - Google Finance rates

## API Response Examples

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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits

This project is developed and maintained by [Carlos J. Ramirez](https://github.com/tomkat-cr). For more information or to contribute to the project, visit [COP Exchange Rates](https://github.com/tomkat-cr/cop-exchange-rates).

Happy Coding!

<br/>

------------------------------

## Español

API de cotización del dólar respecto al Peso Colombiano en Python.<br/>
Incluye actualizaciones de cambio monetarias diarias del dólar de fuentes oficiales de Colombia ([datos.gov.co](https://www.datos.gov.co/)) y otras fuentes como Google Finance ([google.com/finance](https://www.google.com/finance/quote/USD-COP)).

## Tabla de Contenidos

- [Configuración de Desarrollo](#configuración-de-desarrollo)
- [Comandos Disponibles](#comandos-disponibles)
- [Desarrollo Local](#desarrollo-local)
  - [Prerrequisitos](#prerrequisitos)
  - [Instalación](#instalación)
- [Despliegue](#despliegue)
- [Publicación en PyPI](#publicación-en-pypi)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Endpoints de la API](#endpoints-de-la-api)
- [Ejemplos de Respuestas de la API](#ejemplos-de-respuestas-de-la-api)

## Configuración de Desarrollo

### Prerrequisitos

- Python 3.9 - 3.13
- Node.js (para despliegue en Vercel)
- Poetry (recomendado) o pip

### Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tomkat-cr/cop-exchange-rates.git
   cd cop-exchange-rates
   ```

2. **Configurar el entorno:**
   ```bash
   make update  # Instalación limpia con todas las dependencias
   ```

   O manualmente:
   ```bash
   make clean   # Limpiar instalaciones previas
   make run     # Configurar entorno virtual e instalar dependencias
   ```

## Comandos Disponibles

El proyecto incluye un Makefile con los siguientes comandos:

### Comandos de Desarrollo

| Comando | Descripción |
|---------|-------------|
| `make` o `make all` | Mostrar este Makefile |
| `make clean` | Limpiar artefactos de construcción y entorno virtual |
| `make update` | Instalación limpia - elimina configuración existente y reinstala todo |
| `make run` | Configurar entorno virtual y ejecutar la API localmente (devuelve salida JSON) |
| `make run_module` | Ejecutar solo el módulo CLI (igual que "make run") |

### Gestión de Entorno

| Comando | Descripción |
|---------|-------------|
| `make deactivate` | Desactivar el entorno virtual |
| `make pipfile` | Actualizar Pipfile.lock (si se usa pipenv) |

### Comandos de Despliegue

| Comando | Descripción |
|---------|-------------|
| `make run_vercel` | Ejecutar servidor de desarrollo local de Vercel en puerto 5001 |
| `make deploy_prod` | Desplegar a producción en Vercel |
| `make rename_staging` | Renombrar despliegue de staging |

### Comandos de Publicación en PyPI

| Comando | Descripción |
|---------|-------------|
| `make pypi-build` | Construir paquetes de distribución para PyPI |
| `make pypi-publish-test` | Publicar en repositorio de prueba de PyPI |
| `make pypi-publish` | Publicar en PyPI de producción |

## Desarrollo Local

### Inicio Rápido

1. **Ejecutar localmente:**
   ```bash
   make run
   ```
   Esto:
   - Crea un entorno virtual en `cop_exchange_rates/`
   - Instala todas las dependencias
   - Ejecuta la versión CLI y muestra salida JSON

2. **Ejecutar servidor de desarrollo de Vercel:**
   ```bash
   make run_vercel
   ```
   La API estará disponible en `http://localhost:5001`

### Variables de Entorno

Crear un archivo `.env` en la raíz del proyecto para cualquier configuración específica del entorno.

## Despliegue

### Despliegue en Vercel

1. **Desplegar a producción:**
   ```bash
   make deploy_prod
   ```

2. **Ejecutar desarrollo local de Vercel:**
   ```bash
   make run_vercel
   ```

El proyecto está configurado con `vercel.json` para despliegue automático.

## Publicación en PyPI

Este proyecto puede publicarse en PyPI como un paquete de Python:

1. **Construir el paquete:**
   ```bash
   make pypi-build
   ```

2. **Publicación de prueba:**
   ```bash
   make pypi-publish-test
   ```

3. **Publicación de producción:**
   ```bash
   make pypi-publish
   ```

## Estructura del Proyecto

```
cop-exchange-rates/
├── cop_exchange_rates/          # Paquete principal de Python
│   ├── __init__.py
│   ├── index.py                 # Aplicación FastAPI y punto de entrada CLI
│   ├── cop.py                   # Lógica principal de tasas de cambio
│   └── requirements.txt         # Dependencias de Python
├── Makefile                     # Comandos de desarrollo
├── run.sh                       # Script de shell para varias operaciones
├── pyproject.toml              # Configuración de Poetry y metadatos del paquete
├── package.json                # Configuración de Node.js para Vercel
├── vercel.json                 # Configuración de despliegue de Vercel
└── README.md                   # Este archivo
```

## Endpoints de la API

La API proporciona tres endpoints principales:

- `GET /get_exchange_rates` - Tasas combinadas de todas las fuentes
- `GET /get_official_cop` - Tasas oficiales del gobierno colombiano
- `GET /get_google_cop` - Tasas de Google Finance

## Ejemplos de Respuestas de la API

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

## License

Este proyecto está licenciado bajo la Licencia MIT - consulte el archivo [LICENSE](LICENSE) para más detalles.

## Credits

Este proyecto es desarrollado y mantenido por [Carlos J. Ramirez](https://github.com/tomkat-cr). Para más información o para contribuir al proyecto, visite [COP Exchange Rates](https://github.com/tomkat-cr/cop-exchange-rates).

¡Sé Feliz Programando!