import datetime
import os
import re

class FileTools:
    @staticmethod
    def format_to_markdown(text):
        # Split the text into sections based on the pattern
        sections = re.split(r'(\d+\..+?)(?=\n\d+\.|$)', text, flags=re.DOTALL)

        # Apply Markdown formatting
        formatted_text = ""
        for section in sections:
            if section.strip():
                if section.startswith("Title:"):
                    # Format title
                    formatted_text += f"# {section.strip()}\n\n"
                elif re.match(r'\d+\.', section.strip()):
                    # Format section headers and content
                    header, content = section.split('\n', 1)
                    formatted_text += f"## {header.strip()}\n\n{content.strip()}\n\n"
                else:
                    # Regular content
                    formatted_text += f"{section.strip()}\n\n"
        return formatted_text

    @staticmethod
    def write_file(content, filename_prefix="Civic", output_directory="output", extension=".md"):
        """
        Writes a markdown file with the given content to a specified directory. The filename is generated
        using a prefix, the current date and time, and a file extension.

        Parameters:
        - content (str): The content to be written to the file.
        - filename_prefix (str): The prefix for the filename. Defaults to 'Civic'.
        - output_directory (str): The directory where the file will be saved. Defaults to 'output'.
        - extension (str): The file extension to be used. Defaults to '.md'.

        Returns:
        - str: A message indicating success with the file path or an error message.
        """
        try:
            if not re.match(r'^[\w\-. ]+$', filename_prefix):
                raise ValueError("Invalid filename prefix")

            current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            output_filename = f"{filename_prefix}_{current_datetime}{extension}"
            output_file_path = os.path.join(output_directory, output_filename)

            if not os.path.exists(output_directory):
                os.makedirs(output_directory)

            with open(output_file_path, "w") as f:
                f.write(content)

            return f"File successfully written to {os.path.abspath(output_file_path)}"
        except Exception as e:
            return f"Error writing the file: {e}"