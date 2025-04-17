# 🍴 Cafe Order Management System - Django Admin Panel

**Web-based control center for managing Telegram Cafe Bot operations**  
*Seamless integration with PostgreSQL database shared with Telegram bot*

<img src="https://img.shields.io/badge/Django-5.1-green" alt="Django"> <img src="https://img.shields.io/badge/Python-3.10+-blue" alt="Python"> <img src="https://img.shields.io/badge/PostgreSQL-14+-blue" alt="PostgreSQL">

##  Key Features
- **Real-time Menu Management**
  - Add/edit/delete categories and products
  - Unique product names within categories enforcement
- **Order Processing System**
  - View all customer orders with delivery dates
  - Track deleted orders with detailed reasons
- **Advanced Admin Customizations**
  - Custom order deletion flow with reason tracking
  - Enhanced list displays with search/filter capabilities

##  Technology Stack
| Component       | Technology |
|-----------------|------------|
| Backend         | Django 5.1 |
| Database        | PostgreSQL |
| Admin Interface | Django Admin (customized) |

##  Quick Setup

### Prerequisites
- Python 3.10+
- pip

### Installation
```bash
# 1. Clone repository
git clone https://github.com/t1matoma/admin_panel_for_tg_cafe_bot.git
cd admin_panel_for_tg_cafe_bot
```
#### Configure environment  
Create `.env` file (see `.env.example`):  
```ini
DB_HOST=localhost
DB_USER=username
DB_PASSWORD=yourdbpassword
DB_NAME=tg_cafe_bot

SECRET_KEY=example
```

```bash
# 2. Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Linux/Mac
.\.venv\Scripts\activate   # Windows

# 3. Install dependencies
sudo apt update # Linux
sudo apt install python3-dev libpq-dev postgresql-server-dev-all # Linux
pip3 install -r requirements.txt

# 5. Run migrations
cd cafe_admin
python3 manage.py makemigrations orders
python3 manage.py migrate

# 6. Create admin user
python3 manage.py createsuperuser

# 7. Run development server
python3 manage.py runserver
```
##  Environment Configuration

The project uses environment variables for sensitive settings. 
**Never commit your `.env` file to version control!**
