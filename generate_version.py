#!/usr/bin/env python3
"""
Script to generate version files for protobuf protocol versions.
Uses Jinja2 templates to generate mod.rs and version.py files.
"""

import argparse
import os
import sys
from pathlib import Path

try:
    from jinja2 import Environment, FileSystemLoader
except ImportError:
    print("Error: jinja2 is not installed. Please install it with: pip install jinja2")
    sys.exit(1)


def generate_version_files(major_version: int, minor_version: int, output_dir: Path):
    """Generate version.rs and version.py files from Jinja templates."""
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    templates_dir = script_dir / "templates"
    
    if not templates_dir.exists():
        print(f"Error: Templates directory not found: {templates_dir}")
        sys.exit(1)
    
    # Set up Jinja2 environment
    env = Environment(
        loader=FileSystemLoader(str(templates_dir)),
        trim_blocks=True,
        lstrip_blocks=True
    )
    
    # Template variables
    context = {
        "major_version": major_version,
        "minor_version": minor_version,
    }
    
    # Generate version.rs
    rust_template = env.get_template("version.rs.j2")
    rust_output = rust_template.render(**context)
    rust_file = output_dir / "version.rs"
    rust_file.write_text(rust_output)
    print(f"Generated: {rust_file}")
    
    # Generate version.py
    python_template = env.get_template("version.py.j2")
    python_output = python_template.render(**context)
    python_file = output_dir / "version.py"
    python_file.write_text(python_output)
    print(f"Generated: {python_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate version files for protobuf protocol versions"
    )
    parser.add_argument(
        "--major",
        type=int,
        required=True,
        help="Protocol major version number"
    )
    parser.add_argument(
        "--minor",
        type=int,
        required=True,
        help="Protocol minor version number"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default=None,
        help="Output directory (default: same directory as script)"
    )
    
    args = parser.parse_args()
    
    # Determine output directory
    if args.output_dir:
        output_dir = Path(args.output_dir)
    else:
        output_dir = Path(__file__).parent
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    generate_version_files(args.major, args.minor, output_dir)


if __name__ == "__main__":
    main()

