import Foundation

@MainActor
final class ScannerAPI: ObservableObject {
    @Published var dashboard: Dashboard?
    @Published var errorMessage: String?
    @Published var loading = false
    @Published var lastUpdated: Date?

    // Production control is read-only in the first release.
    // Challenger runtime can be selected later without shipping secrets in the client.
    private let controlURL = URL(string: "https://kraken-autonomous-controller-production.up.railway.app")!

    func refresh() async {
        loading = true
        defer { loading = false }
        do {
            var request = URLRequest(url: controlURL.appending(path: "dashboard"))
            request.cachePolicy = .reloadIgnoringLocalCacheData
            request.timeoutInterval = 15
            let (data, response) = try await URLSession.shared.data(for: request)
            guard let http = response as? HTTPURLResponse, 200..<300 ~= http.statusCode else {
                throw URLError(.badServerResponse)
            }
            dashboard = try JSONDecoder().decode(Dashboard.self, from: data)
            errorMessage = nil
            lastUpdated = Date()
        } catch {
            errorMessage = error.localizedDescription
        }
    }
}
