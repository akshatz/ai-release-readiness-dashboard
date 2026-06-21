"""
Release readiness
"""
def calculate_readiness(data):

    score = 0

    if data.development_complete:
        score += 20

    if data.pr_merged:
        score += 15

    if data.staging_deployed:
        score += 20

    if data.qa_complete:
        score += 25

    if data.release_notes_created:
        score += 10

    if data.production_approval:
        score += 10

    return score


def calculate_risk(score):

    if score >= 90:
        return "LOW"

    if score >= 70:
        return "MEDIUM"

    return "HIGH"


def get_blockers(data):

    blockers = []

    if not data.qa_complete:
        blockers.append("QA signoff pending")

    if not data.release_notes_created:
        blockers.append("Release notes missing")

    if not data.production_approval:
        blockers.append("Production approval pending")

    return blockers


def get_recommendations(blockers):

    recommendations = []

    for blocker in blockers:

        if blocker == "QA signoff pending":
            recommendations.append("Complete QA validation")

        elif blocker == "Release notes missing":
            recommendations.append("Generate release notes")

        elif blocker == "Production approval pending":
            recommendations.append("Request production approval")

    return recommendations