import datetime
import os
from langchain.tools import tool

class FileTools():

  @tool("Write Markdown File")
  def write_file(content):
    """
    Useful for writing a markdown file with a given policy task name and content. 
    The file will be saved in the specified output folder with a name 
    based on the policy task and the current date.
    """
    try:
      # Generate file path and name
      current_date = datetime.datetime.now().strftime("%Y-%m-%d")
      output_filename = f"Civic_{current_date}.md"
      output_file_path = os.path.join("output", output_filename)

      # Write to the file
      with open(output_file_path, "w") as f:
        f.write(content)
      return f"File written to {output_file_path}."
    except Exception as e:
      return f"Error writing the file: {e}"
