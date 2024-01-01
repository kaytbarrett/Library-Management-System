using System;
using Newtonsoft.Json;

namespace libraryClient.Components.Models
{
    public class BookViewModel
    {
        [JsonProperty("id")]
        public int Id { get; set; } 
        public string Title { get; set; } = string.Empty;
        public string Author { get; set; } = string.Empty;
        public DateTime PublicationDate { get; set; }
        public decimal Price { get; set; }
        public string Genre { get; set; } = string.Empty;
        public string Publisher { get; set; } = string.Empty;

       // Adjusted to use JsonProperty for proper mapping
        [JsonProperty("cover_image")]
        public string OriginalCoverImage { get; set; } = string.Empty;

        public string CoverImage { get; private set; } = string.Empty;

        // Constructor for initializing default values or additional logic
        public BookViewModel()
        {
            TransformCoverImage();
        }

        private void TransformCoverImage()
        {
            // Check if OriginalCoverImage is not null or empty
            if (!string.IsNullOrEmpty(OriginalCoverImage))
            {
                // Remove any potential leading and trailing whitespaces
                OriginalCoverImage = OriginalCoverImage.Trim();

                // Replace the prefix and decode the URL
                CoverImage = Uri.UnescapeDataString(OriginalCoverImage);
            }
        }
    }
}

