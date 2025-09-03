# Documentation


## Prerequisites
Before running the code in this project, make sure you have the following software installed:
* Python 3.5 and above
* MySQL Community Server 5.7.43
* Libraries: mysql-connector


## MySQL Community Server 5.7.43 Installation
To download and set up MySQL Community Server 5.7.43 with the host as 127.0.0.1, a user, and a password, you can follow these steps:

**Note:** These instructions are for a Windows environment. The steps may vary slightly for other operating systems.

1. **Download MySQL Community Server 5.7.43**:

* Visit the MySQL Community Downloads page: https://dev.mysql.com/downloads/mysql/
* Scroll down to find the MySQL Community Server section.
* Look for the MySQL Community Server version 5.7.43 for Windows. Click on the "Download" button next to it.

2. **Select the Installer**:

* You'll be presented with multiple download options. Choose the "MySQL Installer for Windows" option, which includes all necessary components.

3. **Start the MySQL Installer**:

* Run the downloaded MySQL Installer executable file.

4. **MySQL Installer Setup**:

* You'll be presented with the MySQL Installer Setup wizard. Click "Next."

5. **Choosing a Setup Type**:

* Choose "Server only" and click "Next."

6. **Server Configuration**:

* Select "Standalone MySQL Server / Classic MySQL Replication" and click "Next."

7. **MySQL Server Configuration Type**:

* Choose "Detailed Configuration" and click "Next."

8. **MySQL Server Configuration**:

* Select "Developer Default" as the configuration type. This will set up MySQL with standard settings suitable for development purposes.
* You can choose "Server Computer" as the server type if you want to access the MySQL server from other computers on your network. If you want to restrict it to your local machine (127.0.0.1), you can select "Dedicated Computer."
* Click "Next."

9. **Authentication Method**:

* Choose "Use Legacy Authentication Method (Retain MySQL 5.x Compatibility)" and click "Next."

10. **Set Password for Root Accounts**:

* Enter a strong password for the MySQL root user. Make sure to remember this password as you'll need it later.
* Click "Next."

11. **Configure MySQL as a Windows Service**:

* Leave the "MySQL Server as a Windows Service" option selected.
* You can set the "Service Name" to something like "MySQL57" for easier management.
* Click "Next."

12. **Apply Configuration**:

* Review the configuration settings you've chosen.
* Click "Execute" to apply the configuration.

13. **Installation Complete**:

* Once the configuration is applied successfully, click "Finish."

14. **MySQL Server is Running**:

* MySQL Community Server 5.7.43 is now installed and running on your machine. The host is set to 127.0.0.1 (localhost), and you can use the root user and the password you set during installation to access MySQL.


## MySQL Connector Installation
To install the specific version `2.2.9` of the `mysql-connector` package in Python, you can use `pip`. Here are the steps to install it:

**Note:** The mysql-connector version 2.2.9 is compatible with Python 2.7 and Python 3.x. This means you can use it with Python 2.7 or any version of Python 3. However, please note that Python 2.7 has reached its end of life and is no longer receiving official support or updates from the Python community. It is highly recommended to use Python 3.x.

1. **Open a Command Prompt (Windows) or Terminal (Linux/macOS)**.

2. **Use the following command** to install `mysql-connector` version `2.2.9`:

   ```bash
   pip install mysql-connector==2.2.9
   ```

   This command tells `pip` to install the exact version `2.2.9` of the `mysql-connector` package.

3. **Wait for the installation** to complete. `pip` will download and install the specified version of the package.

4. **Verify the installation**. To ensure that `mysql-connector` version `2.2.9` is successfully installed, you can run the following command to check the installed version:

   ```bash
   pip show mysql-connector
   ```

   This command will display information about the installed package, including its version.


## Database and Table Creation
To run the `schema.sql` file to create the database schema and tables, follow these steps:

1. **Open MySQL Command-Line Client**:

   - Press `Win + R`, type `cmd`, and press Enter to open the Command Prompt.
   - Type the following command to open the MySQL Command-Line Client and press Enter. You need to provide the MySQL root user password you set during installation:

     ```
     mysql -u root -p
     ```

2. **Enter the MySQL Password**:

   - When prompted, enter the password for the MySQL root user and press Enter.


3. **Execute the `schema.sql` File**:

   - Navigate to the directory where the `schema.sql` file is located using the `cd` command in the Command Prompt.

   - Run the following command to execute the SQL script and create the tables and schema:

     ```sql
     source schema.sql;
     ```

     This command reads and executes the SQL statements from the `schema.sql` file.

4. **Verification**:

   - After running the `source` command, MySQL will execute the SQL statements in the `schema.sql` file. If there are no errors, you should see the tables and schema created successfully.

6. **Exit MySQL**:

   - To exit the MySQL Command-Line Client, you can type:

     ```sql
     exit;
     ```

   - Press Enter to exit the client.
