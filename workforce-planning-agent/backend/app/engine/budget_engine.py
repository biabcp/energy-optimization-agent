def summarize(departments):
    budget=sum(d.budget for d in departments); spend=sum(d.current_compensation_spend for d in departments)
    variance=budget-spend; util=(spend/budget*100) if budget else 0
    status="Under budget" if variance>0 else "Over budget"
    return {"approved_budget":budget,"current_spend":spend,"variance":variance,"utilization":round(util,1),"status":status}
