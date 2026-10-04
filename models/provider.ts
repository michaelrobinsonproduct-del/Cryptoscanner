export interface ChangeProposal { summary: string; patch: string; rationale: string }
export interface ModelProvider {
  proposeChange(context: string): Promise<ChangeProposal | null>;
  reviewChange(diff: string, metrics: Record<string, number>): Promise<{approved: boolean; reason: string}>;
}

export class NoopProvider implements ModelProvider {
  async proposeChange(): Promise<null> { return null; }
  async reviewChange(): Promise<{approved: boolean; reason:string}> { return { approved:false, reason:"No model provider configured" }; }
}
