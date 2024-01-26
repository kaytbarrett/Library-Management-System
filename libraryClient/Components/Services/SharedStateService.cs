
namespace libraryClient.Components.Services
{
    public class SharedStateService 
    {
        public event Action OnUserHrefUpdated;

        private string _userHref;

        public string UserHref
        {
            get => _userHref;
            set
            {
                _userHref = value;
                OnUserHrefUpdated?.Invoke();
            }

        }
    }
}