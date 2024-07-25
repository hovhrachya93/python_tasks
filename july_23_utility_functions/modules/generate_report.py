# Create a function to generate a report with both required and optional sections.
# Use positional arguments for required sections.
# Use keyword arguments for optional sections with default values.

def generateReport(title, content, *, footer=""):
    return f"Report Title: {title}\nContent: {content}\nFooter: {footer}"

if __name__ == "__main__":
    print(generateReport("Monthly Report", "This is the content of the report."))
    print(generateReport("Annual Report", "This is the content of the report.", footer="Footer Text"))
