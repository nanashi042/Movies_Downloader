# LegalMovieFinder

**Find legal streaming, purchase, or public-domain download links for movies.**

> ⚠️ **Important:** This project explicitly does **not** provide or link to pirated content. It searches legally-available sources (streaming services, rental/purchase providers, and public-domain archives) and returns direct **legal** links when available.

---

## Features

- Search movies by title (fuzzy match).
- Return metadata: title, year, synopsis, poster.
- Show legal availability:
  - Streaming providers (where available to stream with subscription).
  - Rent / Buy providers (where available to rent or purchase).
  - Public-domain / Creative Commons copies (e.g., Internet Archive).
  - Official YouTube Movies or distributor pages when available.
- Optionally filter results by country (ISO 3166-1 alpha-2).
- CLI and simple Flask web UI examples.

---

## How it works (high level)

1. Query a movie metadata API (e.g., The Movie Database — TMDb) to find the correct title and retrieve metadata.
2. Query provider availability APIs/services:
   - Use official/licensed provider data (e.g., JustWatch API endpoints or other licensed provider APIs) to find where the movie is available legally.
   - Check public-domain repositories (Internet Archive) for freely downloadable legal copies.
3. Aggregate returned links and present them with clear labels (Stream / Rent / Buy / Public Domain).
4. Provide explicit disclaimer for each link about whether it is subscription-based, paid, or free/public-domain.

---

