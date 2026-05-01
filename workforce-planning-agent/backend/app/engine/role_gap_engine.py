def role_gap(role):
    gap = role.target_count - role.current_count - role.open_requisitions
    urgency = "High" if role.criticality=="Critical" and gap>0 else "Medium" if gap>0 else "Low"
    return {"role_title": role.role_title, "department": role.department, "gap_size": gap, "hiring_urgency": urgency}
