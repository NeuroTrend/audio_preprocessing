# audio\_preprocessing

🚧 **Under Active Development** 🚧

Audio File Processing for AI Model Training

This document describes a software application designed to prepare audio files for AI model training. The application automates the process of segmenting AIFF audio files, updating metadata, cataloging them in a database and uploading them to Cloud Storage. The project emphasizes a hexagonal architecture for flexibility and maintainability, with plans to evolve from a local script (V0) to a scalable web service. The document also outlines the repository structure, project mission, implementation steps, and contribution guidelines.

## Table of Contents

- [Repository Structure](#repository-structure)  
- [Introduction](#introduction)  
- [Project Mission Statement](#project-mission-statement)  
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
│   └── frameworks/
│   └── persistence/
├── core/
│   └── domain/
│   └── application/
│   └── repositories/
├── ports/
│   └── outputs/
│   └── inputs/
├── tests/
├── scripts/
├── configs/
├── requirements.txt
├── README.md
├── .gitignore
├── LICENSE
```

## Introduction

The goal of the project is to automate the segmentation and metadata embedding of AIFF audio files to prepare them for AI model training. Storing training data directly on in the AIFF file’s metadata streamlines migrations and the generation of dataset CSV files required by platforms like Hugging Face.

## Project Mission Statement

To simplify the preparation of machine learning audio datasets, facilitating the creation of highly personalized AI models that empower musicians to maximize their impact and reach.

## Project Plan

### Overview

The project will be developed in two main phases:

**MVP (Minimum Viable Product):** A script that operates on a local machine to process audio files, built using hexagonal (ports and adapters) architecture for flexibility and maintainability.

**V1 (Version 1):** Transition the script into a web service deployed on Google Cloud Platform (GCP), enabling scalability and accessibility.

### Architecture

We plan to employ the hexagonal architecture (also known as the ports and adapters pattern) to create a flexible and maintainable codebase. We want to maintain strong separations of concerns, decoupling the core logic from external dependencies. Our goal is to facilitate an easy transition from the MVP to a scalable, cloud native Version 1\.

The application is designed to handle a large number of lossless audio files efficiently. To achieve this, each task operates independently, with queues managing the flow between stages.

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

#### Processing Pipeline

1. Download/Load File into Memory: Retrieve audio files and load them into memory for processing.  
2. Chop the Audio File into Chunks: Split the loaded audio files into smaller chunks for training.  
3. Build & Add Metadata to AIFF and Firestore Database: Embed training metadata into each AIFF chunk and update the Firestore database with relevant information.  
4. Upload the Audio Files into Google Drive: Upload processed audio chunks to Google Drive for storage and easy access with Google Colab.

## Technologies Used

**Programming Language:** Python 3.10.15

**Database:** Google Cloud Firestore

**Cloud Storage:** Google Drive API

**Docker:** Containerization of the application

**Workflow Management:** Workflow execution framework TBD.

## Implementation Steps

### Phase 1: MVP Development

1. ~~Project Setup:~~  
   - ~~Initialize a Git repository and set up the directory structure following hexagonal architecture principles.~~  
   - ~~Create a virtual environment and manage dependencies using requirements.txt.~~  
   - ~~Create a Dockerfile for containerization.~~  
2. Define Ports (Interfaces): Create abstract base classes for each port in the ports/ directory.  
3. Develop Core Services: Implement the AudioProcessor and DatabaseService in the core/ directory.  
   - Ensure they interact only with the defined ports.  
4. Implement Adapters: Implement each port in the adapters/ directory  
   - FileSystemAudioRepository  
   - AIFFMetadataRepository  
   - FirestoreAdapter  
   - GoogleDriveAdapter  
5. Develop Command-Line Interface (CLI)  
6. Testing

# Contributing

Contributions are welcome\! Please open an issue or submit a pull request for any improvements or bug fixes.

# License

This project is licensed under the MIT License.  
