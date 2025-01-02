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

class ProtocolExplainer(Scene):
    
    def construct(self):
        # Create the "SET" text
        set_text = Text("SET").scale(1.5)
        set_text.shift(UP * 2)
        self.play(Write(set_text))
        self.wait(2)

        # Protocol text bits
        protocol_bits = [
            "$3",
            "$3 SET",
            "$3\\r\\nSET",
            "$3\\r\\nSET\\r\\n",
            "$3\r\nSET\r\n",
        ]

        # Create the initial protocol text
        protocol_text = Text(protocol_bits[0]).scale(1.5)
        protocol_text.next_to(set_text, DOWN, buff=1)

        # Add the initial protocol text to the scene
        self.play(Write(protocol_text))
        self.wait(2)

        # Transform the protocol text to reveal each bit
        for bit in protocol_bits[1:]:
            new_protocol_text = Text(bit).scale(1.5)
            new_protocol_text.next_to(set_text, DOWN, buff=1)  # Keep it center-aligned
            self.play(Transform(protocol_text, new_protocol_text))
            self.wait(2)

        # Fade out everything
        self.play(FadeOut(set_text, protocol_text))
        
        # Create the "SET" text
        set_name_alice_text = Text("SET name Alice").scale(1.5)
        set_name_alice_text.shift(UP * 2)
        self.play(Write(set_name_alice_text))
        self.wait(2)
        
        # Protocol text bits
        protocol_bits = [
            "*<array_length> \\r\\n element 1 \\r\\n ... \\r\\n element N \\r\\n",
            "*3 \\r\\n element 1 \\r\\n element 2 \\r\\n element 3 \\r\\n",
            "*3 \\r\\n $3\\r\\nSET \\r\\n $4\\r\\nname \\r\\n $5\\r\\nAlice \\r\\n",
            "*3\\r\\n$3\\r\\nSET\\r\\n$4\\r\\nname\\r\\n$5\\r\\nAlice\\r\\n",
            "*3\r\n$3\r\nSET\r\n$4\r\nname\r\n$5\r\nAlice\r\n",
        ]

        # Create the initial protocol text
        protocol_text = Text(protocol_bits[0]).scale(0.7)
        protocol_text.next_to(set_text, DOWN, buff=1)

        # Add the initial protocol text to the scene
        self.play(Write(protocol_text))
        self.wait(2)

        # Transform the protocol text to reveal each bit
        for bit in protocol_bits[1:]:
            new_protocol_text = Text(bit).scale(0.7)
            new_protocol_text.next_to(set_text, DOWN, buff=1)  # Keep it center-aligned
            self.play(Transform(protocol_text, new_protocol_text))
            self.wait(2)

class DisplayRedisLogo(Scene):
    def construct(self):
        # Load the image
        image = ImageMobject("redis_logo.png")

        # Resize the image (optional)
        image.scale(0.7)  # Scale down by 50%

        # Position the image (optional)
        # image.to_edge(UP)  # Move the image to the top edge

        # Add the image to the scene
        self.add(image)

        # Add some animation (optional)
        self.play(FadeIn(image))  # Animate the image appearing
        self.wait(2)
        self.play(FadeOut(image))  # Animate the image disappearing

class Objectives(Scene):
    def construct(self):
        # Load the image
        objective_1 = Text("Create a simple Redis Server").scale(1)
        objective_2 = Text("Create a simple Redis Client").scale(1)
        objective_3 = Paragraph("Use the Redis Protocol for", "Sending and Receiving Messages", alignment='center').scale(1)
        
        objective_1.shift(UP * 2)
        objective_2.next_to(objective_1, DOWN, buff=1)
        objective_3.next_to(objective_2, DOWN, buff=1)

        self.play(Write(objective_1))
        self.wait(2)
        
        self.play(Write(objective_2))
        self.wait(2)
        
        self.play(Write(objective_3))
        self.wait(2)
        
        self.play(FadeOut(objective_1, objective_2, objective_3))


class KeyValueExplainer(Scene):
    def construct(self):
        key_value_set_basic = Text("key : value").scale(1)
        
        self.play(Write(key_value_set_basic))
        self.wait(2)
                
        key_value_set_basic_string = Text("name : Alice").scale(1)
        
        self.play(Transform(key_value_set_basic, key_value_set_basic_string))
        self.wait(2)
        
        key_value_set_basic_list = Text("colours : [Red, Blue]").scale(1)
        
        self.play(Transform(key_value_set_basic, key_value_set_basic_list))
        self.wait(2)
        
        key_value_set_basic_list_2 = Text("name : Alice,\ncolours : [Red, Blue]").scale(1)
        
        self.play(Transform(key_value_set_basic, key_value_set_basic_list_2))
        self.wait(2)
        
        self.play(FadeOut(key_value_set_basic))
        self.wait(2)
        
        supported_types_left = Paragraph(
            "Simple strings",
            "Simple Errors",
            "Integers",
            "Bulk strings",
            "Arrays",
            "Nulls",
            "Booleans",
            alignment="center",
        ).scale(1)

        supported_types_right = Paragraph(
            "Doubles",
            "Big numbers",
            "Bulk errors",
            "Verbatim strings",
            "Maps",
            "Attributes",
            "Sets",
            "Pushes",
            alignment="center",
        ).scale(1)

        # Position the lists on the left and right of the screen
        supported_types_left.to_edge(LEFT, buff=2)
        supported_types_right.to_edge(RIGHT, buff=2)

        # Play animations to display the lists
        self.play(Write(supported_types_left), Write(supported_types_right))
        self.wait(2)

        # Optional: Add a fade-out effect
        self.play(FadeOut(supported_types_left), FadeOut(supported_types_right))

class HowRedisWorks(Scene):
    def construct(self):
        # Load and position the database image
        database = ImageMobject("database.png")
        database.scale(0.5)  # Adjust size
        database.set_color(WHITE)
        database.to_edge(LEFT, buff=2.5)

        # Load and position the user image
        user = ImageMobject("user.png")
        user.scale(2.5)  # Adjust size
        user.set_color(WHITE)
        user.to_edge(RIGHT, buff=2.5)

        # Create curved arrow from user to database (up then down)
        arrow_to_db = Arrow(
            start=user.get_left(), 
            end=database.get_right(), 
            color=BLUE,
            buff=0.5,
            path_arc=2  # Positive arc goes up first
        )

        # Create curved arrow back to user (down then up)
        arrow_to_user = Arrow(
            start=database.get_right(), 
            end=user.get_left(), 
            color=GREEN,
            buff=0.5,
            path_arc=2  # Negative arc goes down first
        )

        # Display the images
        self.play(FadeIn(database), FadeIn(user))
        self.wait(1)

        # Animate the curved arrows to DB
        self.play(Create(arrow_to_db))
        self.wait(0.5)
        
        # key-value pops up
        key_value = Text("name : Alice").scale(1)
        key_value.next_to(database, UP, buff=1)
        self.play(Write(key_value))
        self.wait(2)
        
        # Animate the curved arrows from DB
        self.play(Create(arrow_to_user))
        self.wait(0.5)
        
        # key-value pops up
        ok = Text("ok").scale(1)
        ok.next_to(user, UP, buff=1)
        self.play(Write(ok))
        self.wait(2)
        
        # Fade out user and arrows
        self.play(
            FadeOut(user), 
            FadeOut(arrow_to_db),
            FadeOut(arrow_to_user),
            FadeOut(ok),
            )
        self.wait(2)
        
        # Re-Display the User
        self.play(FadeIn(user))
        self.wait(2)
        
        self.play(Create(arrow_to_db))
        self.wait(0.5)
        
        self.play(Create(arrow_to_user))
        self.wait(0.5)
        
        # key-value pops up over user
        key_value_2 = Text("name : Alice").scale(1)
        key_value_2.next_to(user, UP, buff=1)
        self.play(Write(key_value_2))
        self.wait(2)
        
        self.play(FadeOut(database), FadeOut(user), FadeOut(arrow_to_db), FadeOut(arrow_to_user), FadeOut(key_value), FadeOut(key_value_2))