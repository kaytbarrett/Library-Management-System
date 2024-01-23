using libraryClient.Components;
using Microsoft.Extensions.DependencyInjection;
using libraryClient.Components.Services;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddRazorComponents()
    .AddInteractiveServerComponents();

// Add named HttpClient configuration with cookie support
builder.Services.AddHttpClient("MyApiClient").ConfigurePrimaryHttpMessageHandler(() => new HttpClientHandler
{
    UseCookies = true
});

builder.Services.AddScoped<IAuthenticationService, AuthenticationService>();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error", createScopeForErrors: true);
    app.UseHsts();
}


app.UseStaticFiles();
app.UseAntiforgery();

app.MapRazorComponents<App>()
    .AddInteractiveServerRenderMode();

app.Run();

