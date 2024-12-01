# audio_preprocessing
🚧 **Under Active Development** 🚧

Audio File Processing for AI Model Training

An application that automates segmentation of AIFF audio files, updates metadata, catalogs them in a database, and uploads them to Google Drive for AI model training preparation.

## Table of Contents

- [Repository Structure](#repository-structure)
- [Introduction](#introduction)
- [Project Purpose](#project-purpose)
- [Project Plan](#project-plan)
- [Overview](#overview)
- [Architecture](#architecture)
- [Technologies Used](#technologies-used)
- [Implementation Steps](#implementation-steps)
- [Contributing](#contributing)
- [License](#license)

## Repository Structure
```
audio_preprocessing/
├── adapters/
│   ├── __init__.py
│   ├── audio_repository.py
│   ├── metadata_repository.py
│   ├── database_adapter.py
│   └── cloud_storage_adapter.py
├── core/
│   ├── __init__.py
│   ├── audio_processor.py
│   └── database_service.py
├── ports/
│   ├── __init__.py
│   ├── audio_repository_port.py
│   ├── metadata_repository_port.py
│   ├── database_port.py
│   └── cloud_storage_port.py
├── tests/
│   ├── __init__.py
│   ├── test_audio_processor.py
│   ├── test_database_service.py
│   ├── test_adapters.py
│   └── fixtures/
├── scripts/
│   └── process_audio.py
├── configs/
│   ├── config.yaml
│   └── logging.yaml
├── requirements.txt
├── README.md
├── .gitignore
├── LICENSE
```

## Introduction

The goal of the project is to automate the segmentation and metadata embedding of AIFF audio files to prepare them for AI model training. By storing training information directly within the AIFF file’s metadata, it streamlines the generation of dataset CSV files required by platforms like Hugging Face.

## Project Mission Statement

To simplify the preparation of machine learning audio datasets, facilitating the creation of highly personalized AI models that empower musicians to maximize their impact and reach.

## Project Plan

### Overview

The project will be developed in two main phases:

**MVP (Minimum Viable Product):** A script that operates on a local machine to process audio files, built using hexagonal (ports and adapters) architecture for flexibility and maintainability.

**Version 1 (V1):** Transition the script into a web service deployed on Google Cloud Platform (GCP), enabling scalability and accessibility.

### Architecture

The application will follow the Hexagonal Architecture (also known as Ports and Adapters) to ensure a clean separation of concerns between the core business logic and external systems.

#### Domain Logic (Core):
Audio Processor Service: Handles the segmentation of audio files and updates metadata.

Database Service: Manages interactions with the database for storing metadata and file references.
#### Ports (Interfaces):
Audio Repository Port: Interface for loading and saving audio files.

Metadata Repository Port: Interface for reading and writing audio metadata.

Database Port: Interface for database operations.

Cloud Storage Port: Interface for uploading files to Google Drive.
#### Adapters (Implementations):

File System Adapter: Implements file operations on the local system.

AIFF Metadata Adapter: Implements metadata operations using suitable libraries.

Firestore Adapter: Implements database operations using Google Cloud Firestore.

Google Drive Adapter: Implements cloud storage operations using the Google Drive API.

## Technologies Used

**Programming Language:** Python 3.10.15

**Database:** Google Cloud Firestore

**Cloud Storage:** Google Drive API

**Docker:** Containerization of the application

## Implementation Steps

### Phase 1: MVP Development

1. ~~Project Setup:~~
    - ~~Initialize a Git repository and set up the directory structure following hexagonal architecture principles.~~
    - ~~Create a virtual environment and manage dependencies using requirements.txt.~~
    - ~~Create a Dockerfile for containerization.~~
2.	Define Ports (Interfaces):
    - Create abstract base classes for each port in the ports/ directory.
3.	Develop Core Services:
    - Implement the AudioProcessor and DatabaseService in the core/ directory.
    - Ensure they interact only with the defined ports.
4.	Implement Adapters:
    - In the adapters/ directory, create concrete implementations for each port:
    - FileSystemAudioRepository
    - AIFFMetadataRepository
    - FirestoreAdapter
    - GoogleDriveAdapter
5.	Develop Command-Line Interface (CLI):
    - Create a script in the scripts/ directory to serve as the entry point.
    - Use argparse or click for handling command-line arguments.
6.	Testing:
    - Write unit tests in the tests/ directory.
    - Use pytest and mocking for testing core logic and adapters.
8.	Documentation:
    - Document the code with docstrings and comments.
    - Update the README.md with usage instructions.

# Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

# License

This project is licensed under the MIT License.
