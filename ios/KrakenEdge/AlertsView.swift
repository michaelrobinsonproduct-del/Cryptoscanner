import SwiftUI
struct AlertsView: View { let candidates:[Candidate]; var body: some View { List(candidates.filter{$0.decision=="PROMOTION_ELIGIBLE"}){c in NavigationLink{CandidateDetailView(candidate:c)}label:{VStack(alignment:.leading){Text(c.pair).font(.headline);Text("Passed independent promotion gates").font(.caption).foregroundStyle(.secondary)}}}.navigationTitle("Alerts") } }
