import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import pandas as pd
import random
from datetime import datetime, timedelta

class ScheduleGenerator:
	def __init__(self, root):
		self.root = root
		self.root.title("Random Schedule Generator")

		self.fields = []

		# Main Frame
		main_frame = ttk.Frame(root, padding="10")
		main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

		# Start Date
		ttk.Label(main_frame, text="Start Date:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
		self.start_date_entry = DateEntry(main_frame, date_pattern='yyyy-mm-dd')
		self.start_date_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

		# End Date
		ttk.Label(main_frame, text="End Date:").grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
		self.end_date_entry = DateEntry(main_frame, date_pattern='yyyy-mm-dd')
		self.end_date_entry.grid(row=0, column=3, padx=5, pady=5, sticky=tk.W)

		# Add Field Button
		self.add_field_button = ttk.Button(main_frame, text="Add Day Configuration", command=self.add_field)
		self.add_field_button.grid(row=0, column=4, padx=5, pady=5)

		# Generate Button
		self.generate_button = ttk.Button(main_frame, text="Generate Schedule", command=self.prompt_filename)
		self.generate_button.grid(row=0, column=5, padx=5, pady=5)

		# Field Frame
		self.field_frame = ttk.Frame(main_frame)
		self.field_frame.grid(row=1, column=0, columnspan=6, pady=10, sticky=tk.EW)

		# Configure grid weights
		main_frame.columnconfigure(1, weight=1)
		main_frame.columnconfigure(3, weight=1)

	def add_field(self):
		row = len(self.fields) * 3  # Each field takes up 3 rows
		
		# Day Configuration
		day_var = tk.StringVar()
		prob_var = tk.DoubleVar()
		time_prob_var = tk.DoubleVar()
		min_time_var = tk.StringVar()
		max_time_var = tk.StringVar()
		min_ampm_var = tk.StringVar(value="AM")
		max_ampm_var = tk.StringVar(value="AM")
		comments_var = tk.StringVar()
		randomize_comments_var = tk.BooleanVar(value=False)
		
		day_label = ttk.Label(self.field_frame, text="Day:")
		day_label.grid(row=row, column=0, padx=5, pady=5, sticky=tk.W)
		day_entry = ttk.Combobox(self.field_frame, textvariable=day_var, values=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], width=10)
		day_entry.grid(row=row, column=1, padx=5, pady=5, sticky=tk.W)
		
		prob_label = ttk.Label(self.field_frame, text="Day Probability (%):")
		prob_label.grid(row=row, column=2, padx=5, pady=5, sticky=tk.W)
		prob_entry = ttk.Entry(self.field_frame, textvariable=prob_var, width=5)
		prob_entry.grid(row=row, column=3, padx=5, pady=5, sticky=tk.W)
		
		# Comments Button
		comments_button = ttk.Button(self.field_frame, text="Comments", command=lambda: self.open_comments_window(comments_var, randomize_comments_var))
		comments_button.grid(row=row, column=4, padx=5, pady=5, sticky=tk.W)
		
		# Delete Button
		delete_button = ttk.Button(self.field_frame, text="Delete", command=lambda: self.delete_field(field_widgets))
		delete_button.grid(row=row, column=5, padx=5, pady=5, sticky=tk.W)
		
		# Time Configuration
		time_prob_label = ttk.Label(self.field_frame, text="Time Probability (%):")
		time_prob_label.grid(row=row+1, column=0, padx=5, pady=5, sticky=tk.W)
		time_prob_entry = ttk.Entry(self.field_frame, textvariable=time_prob_var, width=5)
		time_prob_entry.grid(row=row+1, column=1, padx=5, pady=5, sticky=tk.W)
		
		min_time_label = ttk.Label(self.field_frame, text="Start Time:")
		min_time_label.grid(row=row+1, column=2, padx=5, pady=5, sticky=tk.W)
		min_time_entry = ttk.Entry(self.field_frame, textvariable=min_time_var, width=5)
		min_time_entry.grid(row=row+1, column=3, padx=5, pady=5, sticky=tk.W)
		min_ampm_entry = ttk.Combobox(self.field_frame, textvariable=min_ampm_var, values=["AM", "PM"], width=3)
		min_ampm_entry.grid(row=row+1, column=4, padx=5, pady=5, sticky=tk.W)
		
		max_time_label = ttk.Label(self.field_frame, text="End Time:")
		max_time_label.grid(row=row+1, column=5, padx=5, pady=5, sticky=tk.W)
		max_time_entry = ttk.Entry(self.field_frame, textvariable=max_time_var, width=5)
		max_time_entry.grid(row=row+1, column=6, padx=5, pady=5, sticky=tk.W)
		max_ampm_entry = ttk.Combobox(self.field_frame, textvariable=max_ampm_var, values=["AM", "PM"], width=3)
		max_ampm_entry.grid(row=row+1, column=7, padx=5, pady=5, sticky=tk.W)
		
		# Separator
		separator = ttk.Separator(self.field_frame, orient='horizontal')
		separator.grid(row=row+2, column=0, columnspan=8, sticky='ew', pady=5)
		
		field_widgets = (day_label, day_entry, prob_label, prob_entry, comments_button, delete_button,
						time_prob_label, time_prob_entry, min_time_label, min_time_entry,
						min_ampm_entry, max_time_label, max_time_entry, max_ampm_entry, separator)
		
		self.fields.append((day_var, prob_var, time_prob_var, min_time_var, min_ampm_var, max_time_var, max_ampm_var, comments_var, randomize_comments_var, field_widgets))

	def open_comments_window(self, comments_var, randomize_comments_var):
		comments_window = tk.Toplevel(self.root)
		comments_window.title("Enter Comments")
		
		ttk.Label(comments_window, text="Enter comments (one per line):").grid(row=0, column=0, padx=10, pady=10)
		comments_text = tk.Text(comments_window, width=40, height=10)
		comments_text.grid(row=1, column=0, padx=10, pady=10)
		
		# Load existing comments
		comments_text.insert(tk.END, comments_var.get())
		
		def on_save():
			comments_var.set(comments_text.get("1.0", tk.END).strip())
			comments_window.destroy()
		
		save_button = ttk.Button(comments_window, text="Save", command=on_save)
		save_button.grid(row=2, column=0, pady=10)
		
		# Randomize Toggle
		randomize_check = ttk.Checkbutton(comments_window, text="Randomize Comments", variable=randomize_comments_var)
		randomize_check.grid(row=3, column=0, pady=5)

	def delete_field(self, field_widgets):
		# Remove widgets from the UI
		for widget in field_widgets:
			widget.grid_forget()
			widget.destroy()
		
		# Remove the field from the list
		self.fields = [field for field in self.fields if field[-1] != field_widgets]

	def prompt_filename(self):
		# Create a new Toplevel window for filename input
		filename_window = tk.Toplevel(self.root)
		filename_window.title("Enter Filename")
		
		ttk.Label(filename_window, text="Enter the name for the Excel file:").grid(row=0, column=0, padx=10, pady=10)
		filename_var = tk.StringVar()
		filename_entry = ttk.Entry(filename_window, textvariable=filename_var)
		filename_entry.grid(row=0, column=1, padx=10, pady=10)
		
		def on_confirm():
			filename = filename_var.get().strip()
			if filename:
				if not filename.endswith('.xlsx'):
					filename += '.xlsx'
				self.generate_schedule(filename)
				filename_window.destroy()
			else:
				messagebox.showerror("Error", "Filename cannot be empty.")
		
		confirm_button = ttk.Button(filename_window, text="Confirm", command=on_confirm)
		confirm_button.grid(row=1, column=0, columnspan=2, pady=10)

	def generate_schedule(self, filename):
		try:
			start_date = datetime.strptime(self.start_date_entry.get(), "%Y-%m-%d")
			end_date = datetime.strptime(self.end_date_entry.get(), "%Y-%m-%d")
			if start_date >= end_date:
				raise ValueError("Start date must be before end date.")
			
			date_range = (end_date - start_date).days
			schedule = []
			weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
			
			for i in range(date_range):
				current_date = start_date + timedelta(days=i)
				day_name = current_date.strftime("%A")
				
				for day_var, prob_var, time_prob_var, min_time_var, min_ampm_var, max_time_var, max_ampm_var, comments_var, randomize_comments_var, _ in self.fields:
					target_day = day_var.get()
					target_index = weekdays.index(target_day)
					
					# Select the day based on probability
					if prob_var.get() == 100:
						selected_day = target_day
					else:
						# Calculate weights for nearby days
						weights = [0] * 7
						for offset in range(-3, 4):  # Consider days within a 3-day window
							day_index = (target_index + offset) % 7
							distance = abs(offset)
							weights[day_index] = max(0, 1 - (distance * (1 - prob_var.get() / 100)))
						
						# Normalize weights
						total_weight = sum(weights)
						if total_weight > 0:
							weights = [w / total_weight for w in weights]
						
						# Select a day based on weights
						selected_day = random.choices(weekdays, weights=weights, k=1)[0]
					
					if selected_day == day_name:
						min_hour, min_minute = map(int, min_time_var.get().split(':'))
						max_hour, max_minute = map(int, max_time_var.get().split(':'))
						
						# Convert 12-hour time to 24-hour time
						if min_ampm_var.get() == "PM" and min_hour != 12:
							min_hour += 12
						elif min_ampm_var.get() == "AM" and min_hour == 12:
							min_hour = 0
						
						if max_ampm_var.get() == "PM" and max_hour != 12:
							max_hour += 12
						elif max_ampm_var.get() == "AM" and max_hour == 12:
							max_hour = 0
						
						# Generate start and end times
						if time_prob_var.get() == 100:
							start_time_minutes = min_hour * 60 + min_minute
							end_time_minutes = max_hour * 60 + max_minute
						else:
							start_time_minutes = self.generate_random_time(min_hour, min_minute, max_hour, max_minute, time_prob_var.get())
							end_time_minutes = self.generate_random_time(min_hour, min_minute, max_hour, max_minute, time_prob_var.get())
						
						start_hour = start_time_minutes // 60
						start_minute = start_time_minutes % 60
						end_hour = end_time_minutes // 60
						end_minute = end_time_minutes % 60
						
						start_time = f"{start_hour % 12 or 12}:{start_minute:02} {'AM' if start_hour < 12 else 'PM'}"
						end_time = f"{end_hour % 12 or 12}:{end_minute:02} {'AM' if end_hour < 12 else 'PM'}"
						
						# Calculate duration
						duration_minutes = end_time_minutes - start_time_minutes
						duration_hours = duration_minutes // 60
						duration_remaining_minutes = duration_minutes % 60
						duration = f"{duration_hours}h {duration_remaining_minutes}m"
						
						# Handle comments
						comments = comments_var.get().splitlines()
						if randomize_comments_var.get() and comments:
							comment = random.choice(comments)
						else:
							comment = self.get_grouped_comment(comments, i, date_range) if comments else ""
						
						schedule.append({
							"Date": current_date.strftime("%Y-%m-%d"),
							"Day": day_name,
							"Start Time": start_time,
							"End Time": end_time,
							"Duration": duration,
							"Comment": comment
						})
			
			df = pd.DataFrame(schedule)
			df.to_excel(filename, index=False)
			messagebox.showinfo("Success", f"Schedule generated and saved as '{filename}'.")
		
		except Exception as e:
			messagebox.showerror("Error", str(e))

	def generate_random_time(self, min_hour, min_minute, max_hour, max_minute, probability):
		min_total_minutes = min_hour * 60 + min_minute
		max_total_minutes = max_hour * 60 + max_minute
		time_range = range(min_total_minutes, max_total_minutes + 1)
		
		# Calculate weights for time selection
		midpoint = (min_total_minutes + max_total_minutes) // 2
		time_weights = []
		for t in time_range:
			distance = abs(t - midpoint)
			weight = max(0, 1 - (distance * (1 - probability / 100)))
			time_weights.append(weight)
		
		# Normalize time weights
		total_time_weight = sum(time_weights)
		if total_time_weight > 0:
			time_weights = [w / total_time_weight for w in time_weights]
		
		# Select time based on weights
		selected_time = random.choices(time_range, weights=time_weights, k=1)[0]
		return selected_time

	def get_grouped_comment(self, comments, index, total_dates):
		num_comments = len(comments)
		if num_comments == 0:
			return ""
		# Calculate the number of dates per comment
		dates_per_comment = total_dates // num_comments
		# Determine which comment to use based on the index
		comment_index = min(index // dates_per_comment, num_comments - 1)
		return comments[comment_index]

if __name__ == "__main__":
	root = tk.Tk()
	app = ScheduleGenerator(root)
	root.mainloop()