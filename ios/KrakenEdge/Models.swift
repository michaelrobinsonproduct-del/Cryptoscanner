import Foundation

struct Dashboard: Codable {
    let service: String?
    let version: String?
    let mode: String?
    let cycles: Int?
    let running: Bool?
    let last_cycle_at: String?
    let last_error: String?
    let last_result: CycleResult?
}

struct CycleResult: Codable {
    let candidates: [Candidate]?
}

struct Candidate: Codable, Identifiable {
    var id: String { pair }
    let pair: String
    let decision: String?
    let reason: String?
    let score: Double?
    let displacement_pct: Double?
    let extension_pct: Double?
}
