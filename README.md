# ROVE — Full-stack Social Platform

A VS Code-ready ROVE social media project based on the supplied Stitch design ZIPs. The six uploaded archives have been merged into `design-reference/` so the original Stitch HTML, screenshots and design tokens are included for reference.

## Included screens and routes

### Core social experience
- `/` — Home feed
- `/explore` — Explore & discovery
- `/reels` — Reels viewer
- `/messages` — Direct messages
- `/notifications` — Notifications
- `/create` — Create post / media upload
- `/post/:id` — Post detail and comments
- `/post/:id/edit` — Edit post
- `/post/:id/share` — Share post and tag people
- `/profile/me` and `/profile/:username` — My/public profile
- `/connections?tab=followers` — Followers and following lists
- `/settings/edit-profile` — Edit profile
- `/saved` — Saved posts and collections
- `/saved/collections/new` and `/saved/collections/:id` — Collections
- `/followers`/`/following` concepts are reachable through profile stats; `/people` lists suggested creators
- `/search` — Search results
- `/hashtag/:tag` — Hashtag detail
- `/people` — Suggested people

### Settings, safety and help
- `/settings` — Settings hub
- `/settings/privacy` — Privacy controls
- `/settings/blocked` — Blocked accounts
- `/report` — Report content/user
- `/help` — Help & Support
- `/help/contact` — Contact support
- `/help/report-problem` — Report a technical problem

### Authentication
- `/login` — Login
- `/signup` — Sign up
- `/forgot-password` — Password reset request

## Technology
- Frontend: React, TypeScript, Vite, React Router, Lucide icons
- Backend: Django REST Framework, SQLite, JWT authentication, local media uploads
- Styling: ROVE Plum / Purple / Lavender / White theme

## Run in VS Code (Windows)

### 1. Start the backend
Open a terminal in VS Code:

```powershell
cd backend
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py makemigrations social
python manage.py migrate
python manage.py seed_demo
python manage.py createsuperuser
python manage.py runserver
```

Backend API: `http://127.0.0.1:8000/api/`
Django admin: `http://127.0.0.1:8000/admin/`

If PowerShell blocks virtual-environment activation, run this once in that terminal:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### 2. Start the frontend
Open a **second** VS Code terminal:

```powershell
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173`.

The frontend expects the backend at `http://127.0.0.1:8000/api`. To change it, create `frontend/.env` with:

```env
VITE_API_URL=http://127.0.0.1:8000/api
```

Restart Vite after changing `.env`.

## First-time usage
1. Start the Django backend and Vite frontend.
2. Open `/signup` and create a user (password must pass Django's password validation).
3. Sign in at `/login`.
4. Create a post, like/comment/save posts, edit profile, follow creators and test privacy/report/help forms.
5. Use `/admin/` to inspect posts, reports, support requests, comments and other records.

## API endpoints
- `POST /api/auth/register/`, `POST /api/auth/token/`, `POST /api/auth/token/refresh/`, `GET /api/auth/me/`
- `GET/POST /api/posts/`, `GET/PATCH/DELETE /api/posts/:id/`
- `POST /api/posts/:id/like/`, `POST /api/posts/:id/bookmark/`, `GET/POST /api/posts/:id/comments/`
- `GET/PATCH /api/profiles/me/`, `GET/PATCH /api/profiles/:username/`
- `GET/POST /api/follows/`, `GET /api/bookmarks/`, `GET/POST /api/collections/`
- `GET/POST /api/messages/`, `GET/POST /api/notifications/`
- `GET/PATCH /api/privacy/`, `GET/POST /api/blocked/`, `DELETE /api/blocked/:username/`
- `POST /api/reports/`, `POST /api/support/`, `POST /api/auth/password-reset/`

## Notes and current limitations
- This is a runnable starter application, not a deployed production service. The database is local SQLite.
- Social posts, comments, likes, follows, bookmarks, collections, direct messages, notifications, privacy settings, blocked accounts, reports and support requests have backend models/API endpoints. Use a logged-in account for protected actions.
- The UI includes realistic demonstration content and external Unsplash image URLs in places where no user-uploaded media exists. Those sample images require internet access. Uploaded post images are stored locally in `backend/media/`.
- Password reset returns a generic privacy-preserving confirmation; actual email delivery needs an email provider and credentials.
- Direct messaging is API-backed, but live WebSocket delivery/read receipts are not included yet.
- Third-party OAuth, production security hardening, moderation workflows, automated tests and deployment configuration are not configured.
- `design-reference/` contains the uploaded Stitch HTML/screenshots and the supplied ROVE design-system notes; the React pages implement a connected application experience using the same design direction.

## Production reminder
Before deployment, replace the development `SECRET_KEY`, set `DEBUG=False`, configure production hosts/CORS/HTTPS, use a production database and object storage, configure email delivery, and run automated tests.

## Fixes in this version
- Unauthenticated visitors are redirected to `/login`; protected pages require a valid access token.
- Logout clears the saved JWT tokens and returns to the login screen.
- Likes use the backend response to update the heart, liked label and count; post detail loads real comments and allows adding comments.
- Edit Profile supports selecting an image, previewing it, and uploading it to the Django media folder when Save Changes is clicked.

If you test likes and comments on a fresh database, run `python manage.py seed_demo` after migrations so sample posts exist in the database. Use an account you created through Sign Up to test interactions.
