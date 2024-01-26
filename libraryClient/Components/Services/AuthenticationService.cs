using Microsoft.JSInterop;

namespace libraryClient.Components.Services
{ 
    public class AuthenticationService : IAuthenticationService
    {
        private const string TokenStorageKey = "authToken";
        private const string UserIdStorageKey = "userId";
        private string _token;
        private int _userId;

        private readonly IJSRuntime _jsRuntime;

        public AuthenticationService(IJSRuntime jsRuntime)
        {
            _jsRuntime = jsRuntime;
        }

        public void SetToken(string token, int userId)
        {
            _token = token;
            _userId = userId;
            StoreTokenLocally(token, userId);
            // Additional actions related to setting the token and userId, if needed
        }

        public bool IsAuthenticated()
        {
            // Implement logic to check if the user is authenticated based on your requirements
            // For example, you can check if the token is present and not expired
            return !string.IsNullOrEmpty(_token);
        }

        // Other authentication-related methods or properties can be implemented here

        // Private methods for token storage
        private async Task StoreTokenLocally(string token, int userId)
        {
            await _jsRuntime.InvokeVoidAsync("localStorage.setItem", TokenStorageKey, token);
            await _jsRuntime.InvokeVoidAsync("localStorage.setItem", UserIdStorageKey, userId.ToString());
        }

        // Additional methods for retrieving and clearing the stored userId, if needed
        public async Task<int?> RetrieveUserIdLocally()
        {
            string userIdString = await _jsRuntime.InvokeAsync<string>("localStorage.getItem", UserIdStorageKey);
            if (int.TryParse(userIdString, out int userId))
            {
                return userId;
            }
            return null;
        }

        public async Task ClearUserIdLocally()
        {
            await _jsRuntime.InvokeVoidAsync("localStorage.removeItem", UserIdStorageKey);
        }
    }
}
