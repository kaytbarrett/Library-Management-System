namespace libraryClient.Components.Services
{
    public interface IAuthenticationService
    {
    void SetToken(string token);
    bool IsAuthenticated();
    // Other authentication-related methods or properties can be added here
    }
}