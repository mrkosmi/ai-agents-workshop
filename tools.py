from google.genai import types

tools = [
    types.Tool(
        function_declarations=[
            types.FunctionDeclaration(
                name="get_files_info",
                description="List files in a directory",
                parameters=types.Schema(
                    type=types.Type.OBJECT,
                    properties={
                        "directory": types.Schema(
                            type=types.Type.STRING
                        ),
                    },
                ),
            ),
            types.FunctionDeclaration(
                name="get_file_content",
                description="Read file content",
                parameters=types.Schema(
                    type=types.Type.OBJECT,
                    properties={
                        "file_path": types.Schema(
                            type=types.Type.STRING
                        ),
                    },
                ),
            ),
            types.FunctionDeclaration(
                name="write_file",
                description="Write content to file",
                parameters=types.Schema(
                    type=types.Type.OBJECT,
                    properties={
                        "file_path": types.Schema(
                            type=types.Type.STRING
                        ),
                        "content": types.Schema(
                            type=types.Type.STRING
                        ),
                    },
                ),
            ),
        ]
    )
]