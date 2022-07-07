#python script by rikardoroa
#just python it!

import numpy as np
import pandas as pd
import os


class Vamstar_challenge:

    def __init__(self, weight=np.zeros([0, 0], dtype=np.int32),
                 height=np.zeros([0, 0], dtype=np.int32),
                 gender=np.zeros([0, 0], dtype=np.int32),
                 bmi_data=pd.DataFrame()):

        """init function to initialize all the variables or objects """
        self.weight = weight
        self.height = height
        self.gender = gender
        self.bmi_data = bmi_data

    def random_values(self):
        """this function create 1 million of random values using a numpy array,
           this values correspond to height, weight and gender like this:
           height random values between 150cm - 160cm
           weight random values between 50Kg - 100Kg
           gender random values between 1 - 3
        """
        try:
            self.height = np.random.randint(150, 180, 1000000).tolist()
            self.weight = np.random.randint(50, 100, 1000000).tolist()
            self.gender = np.random.randint(1, 3, 1000000).tolist()
            return self.weight, self.height, self.gender
        except Exception as e:
            print(e)

    def data_gen_and_filtering(self):
        """this function normalize gender using pandas and also
           the calculation of BMI applying the formula KG / (Height)^2 following this steps:
           1) Height / 100
           2) Height^2 = Height * Height
           3) BMI = Weight / Height^2

           to achieve the previous step, it's use the function bmi(x),
           for the normalization of gender  applied a lambdas function to determine 1 for female and 2 for male

           to achieve bmi category and health risk, it's use the lambda functions bmi_category(x)
           and health_risk(x) respectably
        """
        try:
            self.bmi_data = pd.DataFrame(self.gender)
            self.bmi_data = self.bmi_data.rename(columns={0: 'Gender'})
            self.bmi_data['Gender'] = self.bmi_data['Gender'].astype(str)
            self.bmi_data['Gender'] = self.bmi_data['Gender'].apply(
                lambda x: x.replace('1', 'Female') if x == '1' else x.replace('2', 'Male'))
            height = pd.Series(self.height)
            self.bmi_data['HeightCm'] = height
            weight = pd.Series(self.weight)
            self.bmi_data['Weightkg'] = weight
            self.bmi_data['HeightCm'] = self.bmi_data['HeightCm'] / 100
            self.bmi_data['BMI'] = self.bmi_data.apply(lambda x: self.bmi(x['HeightCm'], x['Weightkg']), axis=1)
            self.bmi_data['BMI'] = self.bmi_data['BMI'].apply(lambda x: round(x, 2))
            self.bmi_data['BMI_category'] = self.bmi_data['BMI'].apply(lambda x: self.bmi_category(x))
            self.bmi_data['Health_risk'] = self.bmi_data['BMI_category'].apply(lambda x: self.health_risk(x))
            print(self.bmi_data.head())
        except Exception as e:
            print(e)

    def bmi_category_count(self):
        """this function uses pandas loc filtering to count all the BMI Categories like this:
           df.loc[(condition1) & (condition2)].shape[0], to determine the numbers of rows that
           fills the conditions
        """
        try:
            Overweight = self.bmi_data.loc[(self.bmi_data.BMI >= 25) & (self.bmi_data.BMI < 30)].shape[0]
            Underweight = self.bmi_data.loc[self.bmi_data.BMI <= 18.4].shape[0]
            Normal_weight = self.bmi_data.loc[(self.bmi_data.BMI >= 18.5) & (self.bmi_data.BMI < 25)].shape[0]
            Moderately_obese = self.bmi_data.loc[(self.bmi_data.BMI >= 30) & (self.bmi_data.BMI < 35)].shape[0]
            Severely_obese = self.bmi_data.loc[(self.bmi_data.BMI >= 35) & (self.bmi_data.BMI < 40)].shape[0]
            Very_severely_obese = self.bmi_data.loc[self.bmi_data.BMI >= 40].shape[0]
            print(f"Total Persons with Overweight:{Overweight}")
            print(f"Total Persons with Underweight:{Underweight}")
            print(f"Total Persons with Normal_weight:{Normal_weight}")
            print(f"Total Persons with Moderately obese:{Moderately_obese}")
            print(f"Total Persons with Severely obese:{Severely_obese}")
            print(f"Total Persons with Very severely obese:{Very_severely_obese}")
        except Exception as e:
            print(e)

    @staticmethod
    def bmi_category(x):
        try:
            if x < 18.4:
                return "Underweight"
            if 18.5 <= x <= 24.9:
                return "Normal weight"
            if 25 <= x <= 29.9:
                return "Overweight"
            if 30 <= x <= 34.9:
                return "Moderately obese"
            if 35 <= x <= 39.9:
                return "Severely obese"
            if x >= 40:
                return "Very Severely obese"
        except Exception as e:
            print(e)

    @staticmethod
    def health_risk(x):
        try:
            if x == "Underweight":
                return "Malnutrition risk"
            if x == "Normal weight":
                return "Low risk"
            if x == "Overweight":
                return "Enhanced risk"
            if x == "Moderately obese":
                return "Medium risk"
            if x == "Severely obese":
                return "High risk"
            if x == "Very Severely obese":
                return "Very high risk"
        except Exception as e:
            print(e)

    @staticmethod
    def bmi(col1, col2):
        try:
            col1 = col1 * col1
            return col2 / col1
        except Exception as e:
            print(e)

    def file_creation(self):
        """this function creates a json file in the root directory of the project,
           this file contains all the DataFrame data (1000.000 records) about Gender,
           Height and Weightkg
        """
        try:
            path = os.path.abspath("BMI_data.json")
            with open(path, "w") as json_file:
                j_file = self.bmi_data.loc[:, ['Gender', 'HeightCm', 'Weightkg']].to_json(orient='records')
                json_file.write(j_file)
        except Exception as e:
            print(e)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    v_challenge = Vamstar_challenge()
    v_challenge.random_values()
    v_challenge.data_gen_and_filtering()
    v_challenge.bmi_category_count()
    v_challenge.file_creation()
