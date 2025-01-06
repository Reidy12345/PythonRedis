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

class ProtocolExplainerString(Scene):
     def construct(self):
        
        set_text = Text("SET").scale(1.5)
        set_text.shift(UP * 2)
        self.play(Write(set_text))
        self.wait(0.5)
        
        full_text = r"$3\\r\\nSET\\r\\n"
        font_size=48
        
        text = Text(full_text, font_size=font_size, color=BLACK)
        self.add(text)
        
        reveal_sequence = [1,1,6,3,6] 
        current_index = 0
        
        # Reveal the characters step by step
        for step_idx, step in enumerate(reveal_sequence):
                    
            next_index = current_index + step

            revealed_text = Text(
                full_text, font_size=font_size
            ).move_to(ORIGIN)
            
            for j in range(len(full_text)):
                if j < next_index:
                    revealed_text[j].set_color(WHITE)
                else:
                    revealed_text[j].set_color(BLACK)

            self.play(Transform(text, revealed_text), run_time=1)

            current_index = next_index
            self.wait(0.2)
                
        final_text_data = "$3\r\nSET\r\n"
        final_text = Text(final_text_data, font_size=font_size)
        self.play(Transform(text, final_text))
 
        self.wait(2)
        

class ProtocolExplainerArray(Scene):
    def construct(self):
        
        set_name_alice_text = Text("SET  name  Alice").scale(1.5)
        set_name_alice_text.shift(UP * 2)
        self.play(Write(set_name_alice_text))
        self.wait(0.5)
        
        full_text = r"*3\\r\\n$3\\r\\nSET\\r\\n$4\\r\\nname\\r\\n$5\\r\\nAlice\\r\\n"
        font_size=36
        
        text = Text(full_text, font_size=font_size, color=BLACK)
        self.add(text)
        
        reveal_sequence = [1,1,6,11,6,12,6,13,6] 
        current_index = 0
        
        under_line_level_start = UP * 1.5 + LEFT * 3.5
        
        set_line = Line(start=under_line_level_start, end=under_line_level_start + RIGHT * 1.7, color=WHITE)
        space_one_line = Line(start=set_line.get_end() + RIGHT * 0.05, end=set_line.get_end() + RIGHT * 0.37 , color=WHITE)
        name_line = Line(start=space_one_line.get_end() + RIGHT * 0.1, end=space_one_line.get_end() + RIGHT * 2.25, color=WHITE)
        space_two_line = Line(start=name_line.get_end() + RIGHT * 0.1, end=name_line.get_end() + RIGHT * 0.38, color=WHITE)
        alice_line = Line(start=space_two_line.get_end() + RIGHT * 0.1, end=space_two_line.get_end() + RIGHT * 2.4, color=WHITE)
        
        lines = dict()
        lines[3] = set_line
        lines[4] = space_one_line
        lines[5] = name_line
        lines[6] = space_two_line
        lines[7] = alice_line
        
        line = None
        
        # Reveal the characters step by step
        for step_idx, step in enumerate(reveal_sequence):
            
            # move the line over the SET name Alice
            current_line = lines.get(step_idx)
            if current_line is not None:
                
                if line is None:
                    line = current_line
                    self.play(Create(line), run_time=1)
                else:
                    self.play(Transform(line, current_line), run_time=1)
                
            next_index = current_index + step

            revealed_text = Text(
                full_text, font_size=font_size
            ).move_to(ORIGIN)
            
            for j in range(len(full_text)):
                if j < next_index:
                    revealed_text[j].set_color(WHITE)
                else:
                    revealed_text[j].set_color(BLACK)

            self.play(Transform(text, revealed_text), run_time=1)

            current_index = next_index
            self.wait(0.2)
                
        final_text_data = "*3\r\n$3\r\nSET\r\n$4\r\nname\r\n$5\r\nAlice\r\n"
        final_text = Text(final_text_data, font_size=font_size).shift(DOWN)
        self.play(Transform(text, final_text), FadeOut(line))
 
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
        objective_1 = Text("Understand the Basics of the Redis Protocol").scale(1)
        objective_2 = Text("Create a simple Redis Client and Server that").scale(1)
        objective_2a = Paragraph("Can store and get", "strings and arrays", "of strings", alignment='center').scale(0.8)
        objective_2b = Paragraph("Uses the Redis Protocol", "for Sending and", "Receiving messages", alignment='center').scale(0.8)        
        
        objective_1.shift(UP * 2)
        objective_2.next_to(objective_1, DOWN, buff=1)
        objective_2a.next_to(objective_2, DOWN, buff=1)
        objective_2b.next_to(objective_2, DOWN, buff=1)
        
        objective_2a.shift(LEFT * 3)
        objective_2b.shift(RIGHT * 3)

        self.play(Write(objective_1))
        self.wait(2)
        
        self.play(Write(objective_2))
        self.wait(2)
        
        self.play(Write(objective_2a))
        self.wait(2)
        
        self.play(Write(objective_2b))
        self.wait(2)
        
        self.play(FadeOut(*self.mobjects))


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

class WhyUseRedisPt1(Scene):
    def construct(self):
        
        redis_image = ImageMobject("redis_logo.png").scale(0.7)
        self.add(redis_image)

        self.play(FadeIn(redis_image))
        self.wait(2)
        
        self.play(redis_image .animate.move_to(LEFT * 2).scale(0.7))
        
        postgres_image = ImageMobject("postgres_logo.png").scale(0.7)
        postgres_image.move_to(RIGHT * 2 + UP * 1.3   ) 
        
        couchbase_image = ImageMobject("couchbase.png").scale(0.1)
        couchbase_image.next_to(postgres_image, DOWN, buff=0.5)
                
        self.play(FadeIn(postgres_image, couchbase_image))
        self.wait(2)
        
        self.play(FadeOut(redis_image, postgres_image, couchbase_image))
        self.wait(2)

class WhyUseRedisPt2(Scene):
    def construct(self):
        
        user = ImageMobject("user.png")
        user.scale(2.5)
        user.set_color(WHITE)
        user.move_to(LEFT * 4) 
                
        redis_image = ImageMobject("redis_logo.png").scale(0.5)
        redis_image.move_to(RIGHT * 4 + UP * 2) 
                
        postgres_image = ImageMobject("postgres_logo.png").scale(0.7)
        postgres_image.move_to(RIGHT * 4 + DOWN * 2)    
             
        self.play(FadeIn(user, redis_image, postgres_image))
        self.wait(2)
        
        curve_angle = -0.1
        
        user_to_redis = ArcBetweenPoints(
            start=user.get_right() + UP * 0.2, 
            end=redis_image.get_left() + LEFT * 0.2, 
            angle=curve_angle,  # Controls the curvature
            color=RED
        )
        
        redis_to_user = ArcBetweenPoints(
            start=redis_image.get_left() + LEFT * 0.2, 
            end=user.get_right() + UP * 0.2, 
            angle=curve_angle,  # Controls the curvature
            color=RED
        )

        user_to_postgres = ArcBetweenPoints(
            start=user.get_right() + DOWN * 0.2, 
            end=postgres_image.get_left(), 
            angle=curve_angle,  # Controls the curvature
            color=BLUE
        )

        postgres_to_user = ArcBetweenPoints(
            start=postgres_image.get_left(), 
            end=user.get_right() + DOWN * 0.2, 
            angle=curve_angle,  # Controls the curvature
            color=BLUE
        )
        
        redis_speed = 3
        postgres_speed = 5
        self.play(
            AnimationGroup(
                Succession(
                    Create(user_to_redis, run_time=redis_speed, rate_func=linear),
                    Create(redis_to_user, run_time=redis_speed, rate_func=linear)
                ),
                Succession(
                    Create(user_to_postgres, run_time=postgres_speed, rate_func=linear),
                    Create(postgres_to_user, run_time=postgres_speed, rate_func=linear)
                ),
                lag_ratio=0
            )
        )
        
        self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
        self.wait(2)