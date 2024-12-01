from src.modes.base_mode import LearningMode

class BasicMode(LearningMode):
    def process_user_edit(self, original_response: str, edited_response: str, context: dict) -> str:
        """Basic mode: direct comparison and preference learning"""
        print("\nAnalyzing changes between responses and user privacy preferences...")
        return self.gpt_interface.learn_preferences(original_response, edited_response, context)