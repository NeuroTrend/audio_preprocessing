---
layout: page  
---

# CLI Command Structure Guide

## Purpose of the CLI

The purpose of the CLI is to allow complete audio preprocessing workflows to be done locally or in the Cloud. Each component of the workflow can also be triggered independently to allow each tool to be used separately or in an entirely new workflow order. The CLI enables comprehensive audio preprocessing workflows to be executed both locally and in the Cloud. It also allows for the independent triggering of each workflow component, facilitating the use of each tool separately or within a completely new workflow sequence.

The CLI’s default behavior prioritizes user-friendliness with a human-first design, without sacrificing crucial features such as flexible cloud deployments (supporting both monolithic and microservices architectures) and robust scripting capabilities.

## Basic Command Structure

### Running a Complete Workflow

Use the command `audio run <workflow_name>` to execute all components of the specified workflow in sequence.

For instance, `audio run fingerprint` will run the entire "fingerprint" workflow.

### Running a Single Component

Use the command `audio component <component_name>` to execute a specific component within a workflow.

For example, `audio component create-hashmaps` will only run the "create-hashmaps" component.

### General Usability:

`-v`, `--verbose`: Increases the verbosity of the output, providing more detailed information about the running processes. This is helpful for both debugging and understanding what's happening under the hood.

`-q`, `--quiet`: Suppresses all non-essential output, making the CLI suitable for scripting and background tasks.

`-h`, `--help`: Displays help information for any command or subcommand. This should provide clear usage instructions and descriptions of available options.

### Scripting and Automation:

`-i`, `--input <path>`: Specifies the path to the input audio file or directory.

`-o`, `--output <path>`: Specifies the path for saving the output.

`-f`, `--format <format>`: Sets the output format (e.g., wav, mp3, json).

`-j --json`: Formats stdout to JSON.

# 🚧 Available Commands 🚧

* List of all available commands  
* Brief description of each command's function

# 🚧 Command Details 🚧

* Detailed explanation of each command  
* Options and arguments specific to each command  
* Examples of command usage

# 🚧 Advanced Usage 🚧

* Chaining commands  
* Piping output  
* Scripting

# 🚧 Troubleshooting 🚧

* Common errors and solutions  
* Tips for debugging
