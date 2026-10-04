import SwiftUI

struct ContentView: View {
    @StateObject private var api = ScannerAPI()
    var body: some View {
        TabView {
            NavigationStack {
                List {
                    Section("System") {
                        LabeledContent("Mode", value: api.dashboard?.mode ?? "—")
                        LabeledContent("Version", value: api.dashboard?.version ?? "—")
                        LabeledContent("Cycles", value: String(api.dashboard?.cycles ?? 0))
                        if let e = api.dashboard?.last_error, !e.isEmpty { Text(e).foregroundStyle(.red) }
                    }
                    Section("Candidates") {
                        ForEach(api.dashboard?.last_result?.candidates ?? []) { c in
                            NavigationLink { CandidateDetailView(candidate: c) } label: {
                                VStack(alignment: .leading, spacing: 4) {
                                    HStack { Text(c.pair).font(.headline); Spacer(); Text(c.decision ?? "WATCH").font(.caption).bold() }
                                    Text(c.reason ?? "No reason").font(.caption).foregroundStyle(.secondary)
                                    Text("Score \(Int(c.score ?? 0)) · displacement \(String(format: "%.2f", c.displacement_pct ?? 0))%").font(.caption2).foregroundStyle(.secondary)
                                }
                            }
                        }
                    }
                }
                .navigationTitle("Kraken Edge")
                .refreshable { await api.refresh() }
                .task { await api.refresh() }
                .toolbar { Button("Refresh") { Task { await api.refresh() } } }
            }.tabItem { Label("Scanner", systemImage:"waveform.path.ecg") }
            NavigationStack { SystemHealthView(dashboard: api.dashboard) }.tabItem { Label("Health",systemImage:"heart.text.square") }
        }
    }
}
