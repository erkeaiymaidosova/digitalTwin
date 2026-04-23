def get_learning_resources(job_name):
    resources = {
        "AI Engineer": [
            "Learn PyTorch on YouTube",
            "Build AI project with Python",
            "Read Kaggle tutorials"
        ],
        "Data Analyst": [
            "Learn SQL basics",
            "Practice Excel dashboards",
            "Study statistics course"
        ],
        "UI UX Designer": [
            "Learn Figma",
            "Study user research",
            "Make mobile app prototype"
        ],
        "Product Manager": [
            "Read product case studies",
            "Learn agile basics",
            "Practice roadmap planning"
        ]
    }

    return resources.get(job_name, ["No resources found"])