namespace libraryClient.Components.Services
{
    public interface IAuthenticationService
    {
    void SetToken(string token, int userId);
    bool IsAuthenticated();
    Task<int?> RetrieveUserIdLocally();
    Task ClearUserIdLocally();
    // Other authentication-related methods or properties can be added here
    }
}