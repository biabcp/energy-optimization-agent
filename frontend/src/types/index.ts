export interface AnalyticsSummary {
  total_kwh?: number;
  estimated_cost?: number;
  monthly_savings_opportunity?: number;
  peak_demand_periods?: Record<string, number>;
  top_machines?: Record<string, number>;
}

export interface Recommendation {
  title: string;
  priority: string;
  recommended_action: string;
}
