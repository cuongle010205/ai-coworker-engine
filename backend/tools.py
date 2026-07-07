# tools.py

from datetime import datetime


class ToolManager:

    def __init__(self):

        self.company_policy = {

            "nda":
                "Confidential company information must never be disclosed.",

            "competency":
                "Vision, Entrepreneurship, Passion, Trust.",

            "mobility":
                "Encourage cross-brand mobility while respecting brand DNA."

        }


    def run(

        self,

        tool_name,

        user_message

    ):

        if tool_name == "policy_lookup":

            return self.policy_lookup(user_message)

        if tool_name == "kpi_calculator":

            return self.kpi_calculator()

        if tool_name == "portfolio_export":

            return self.export_portfolio()

        if tool_name == "progress_tracker":

            return self.progress()

        return ""


    def policy_lookup(

        self,

        question

    ):

        q = question.lower()

        for key in self.company_policy:

            if key in q:

                return self.company_policy[key]

        return "No related company policy found."


    def kpi_calculator(self):

        return {

            "Leadership Adoption": "82%",

            "Training Completion": "76%",

            "Internal Mobility": "18%",

            "Employee Satisfaction": "4.3/5"

        }


    def export_portfolio(self):

        return {

            "Problem Statement":
                "Completed",

            "Competency Matrix":
                "Completed",

            "CEO Deck":
                "Completed"

        }


    def progress(self):

        return {

            "module": 2,

            "task_completed": 5,

            "total_task": 9,

            "updated":

                datetime.now().strftime(

                    "%Y-%m-%d %H:%M"

                )

        }
    def list_tools(self):

        return [

        "policy_lookup",

        "kpi_calculator",

        "portfolio_export",

        "progress_tracker"

    ]