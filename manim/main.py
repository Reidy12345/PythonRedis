from manim import *

class ClientCode(Scene):
    def construct(self):
        
        with open("../Client.py", "r") as file:
            all_lines = file.readlines()
            python_code = "".join(all_lines[5:24])
        
        # Create a Code object with the Python code
        code = Code(
            # file_name="../Client.py",
            code = python_code,
            tab_width=4,
            line_spacing=0.5,
            insert_line_no=True,
            style="monokai",
            language="python",
        ).scale(0.75)
        
        part1 = VGroup(*code.code[:5])
        part2 = VGroup(*code.code[5:])

        self.play(Write(part1), run_time=5)
        self.wait(3)

        self.play(Write(part2), run_time=5)
        self.wait(3)

        # Fade out everything
        self.play(FadeOut(part1, part2))

class ServerCode(Scene):
    def construct(self):
        
        # TODO: Maybe add the imports also? 
        with open("../Server.py", "r") as file:
            all_lines = file.readlines()
            python_code = "".join(all_lines[43:62])
        
        # Create a Code object with the Python code
        code = Code(
            code = python_code,
            tab_width=4,
            line_spacing=0.5,
            insert_line_no=True,
            style="monokai",  # Style for syntax highlighting
            language="python",  # Specify Python as the language
        ).scale(0.8)
        
        # self.play(FadeIn(code.line_numbers))
        
        part1 = VGroup(*code.code[:7])
        part2 = VGroup(*code.code[7:11])
        part3 = VGroup(*code.code[11:16])
        part4 = VGroup(*code.code[16:])
        
        self.play(Write(part1), run_time=5)
        self.wait(2)
        
        self.play(Write(part2), run_time=5)
        self.wait(2)
        
        self.play(Write(part3), run_time=5)
        self.wait(2)
        
        self.play(Write(part4), run_time=5)
        self.wait(2)
        
        self.play(FadeOut(part1, part2, part3, part4))