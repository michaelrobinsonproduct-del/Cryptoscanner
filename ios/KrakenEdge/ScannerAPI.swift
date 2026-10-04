import Foundation

@MainActor
final class ScannerAPI: ObservableObject {
    @Published var dashboard: Dashboard?
    @Published var errorMessage: String?
    @Published var loading = false
    private let baseURL = URL(string: "https://kraken-autonomous-controller-production.up.railway.app")!

    func refresh() async {
        loading = true; defer { loading = false }
        do {
            let (data, response) = try await URLSession.shared.data(from: baseURL.appending(path: "dashboard"))
            guard let http = response as? HTTPURLResponse, 200..<300 ~= http.statusCode else { throw URLError(.badServerResponse) }
            dashboard = try JSONDecoder().decode(Dashboard.self, from: data)
            errorMessage = nil
        } catch { errorMessage = error.localizedDescription }
    }
}
