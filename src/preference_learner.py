import sys
import os
import nltk
from typing import List, Dict, Optional
from nltk.tokenize import word_tokenize
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class PreferenceLearner:
    def __init__(self):
        self.learned_preferences = []
        self.preference_history = []
        try:
            import nltk
            nltk.download('punkt')
            nltk.download('punkt_tab')
        except Exception as e:
            print(f"Warning: NLTK data download failed: {e}")
            print("Falling back to simple string comparison")

    def extract_preferences(self, gpt_analysis: str) -> List[str]:
        """Extract clean preference rules from GPT's analysis"""
        try:
            # Debug print
            print("\nAttempting to extract preferences from:")
            print(gpt_analysis)

            # Find the Summary section
            markers = [
            "Summary of user privacy preferences:",
            "suggests the following privacy preferences:",
            "the user's justifications suggest the following privacy preferences:"
            ]

            summary_section = None
            for marker in markers:
                if marker.lower() in gpt_analysis.lower():
                    print(f"\nFound marker: {marker}")  # Debug print
                    summary_section = gpt_analysis.split(marker, 1)[1].strip()
                    break
            #if "Summary of user privacy preferences:" in gpt_analysis:
            #    summary_section = gpt_analysis.split("Summary of user privacy preferences:")[1].strip()
            
            if summary_section:
                print("\nExtracted summary section:")  # Debug print
                print(summary_section)

                # Extract preferences within curly braces
                preferences = []
                for line in summary_section.split('\n'):
                    if '{' in line and '}' in line:
                        # Extract content between curly braces
                        pref = line[line.find('{')+1:line.find('}')].strip()
                        # Split into information type and disclosure rule
                        info_type, disclosure = [x.strip() for x in pref.split(',', 1)]
                        # Format as clean preference rule
                        preferences.append(f"For {info_type}: {disclosure}")
                
                print("\nExtracted preferences:")  # Debug print
                print(preferences)
                return preferences
            
            print("\nNo summary section found")  # Debug print
            return []
        except Exception as e:
            print(f"Error extracting preferences: {e}")
            return []
    
    def add_preference(self, scenario_number: int, preference_analysis: str):
        """Add new learned preferences"""
        clean_preferences = self.extract_preferences(preference_analysis)
        preference_entry = {
            'scenario_number': scenario_number,
            'preferences': clean_preferences,
            'full_analysis': preference_analysis  # Keep full analysis for reference
        }
        self.learned_preferences.append(preference_entry)
    
    def get_current_preferences(self) -> List[str]:
        """Return just the clean preference rules (for use in prompts)"""
        all_preferences = []
        for entry in self.learned_preferences:
            all_preferences.extend(entry['preferences'])
        return all_preferences

    def get_all_preferences(self) -> List[Dict]:
        """Return all learned preferences with their scenario numbers"""
        return self.learned_preferences
    
    def get_preference_by_scenario(self, scenario_number: int) -> Optional[str]:
        """Get learned preference for a specific scenario"""
        for entry in self.learned_preferences:
            if entry['scenario_number'] == scenario_number:
                return entry['full_analysis']
        return None

    def calculate_edit_distance(self, response1: str, response2: str) -> float:
        """Calculate normalized edit distance between two responses"""
        tokens1 = word_tokenize(response1)
        tokens2 = word_tokenize(response2)
        
        distance = nltk.edit_distance(tokens1, tokens2)
        max_length = max(len(tokens1), len(tokens2))
        
        return distance / max_length if max_length > 0 else 0
    
    def record_interaction(self, scenario_number: int, original: str, edited: str, 
                         learned_preference: str):
        """Record an interaction for analysis"""
        interaction = {
            'scenario_number': scenario_number,
            'original_response': original,
            'edited_response': edited,
            'learned_preference': learned_preference,
            'edit_distance': self.calculate_edit_distance(original, edited)
        }
        self.preference_history.append(interaction)
    
    def get_learning_progress(self) -> Dict:
        """Get metrics about learning progress"""
        if not self.preference_history:
            return {
                'total_interactions': 0,
                'average_edit_distance': 0.0,
                'preference_count': 0
            }
            
        edit_distances = [inter['edit_distance'] for inter in self.preference_history]
        return {
            'total_interactions': len(self.preference_history),
            'average_edit_distance': sum(edit_distances) / len(edit_distances),
            'preference_count': len(self.learned_preferences)
        }

    def reset(self):
        """Reset all learned preferences and history"""
        self.learned_preferences = []
        self.preference_history = []