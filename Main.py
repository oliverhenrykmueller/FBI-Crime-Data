# -*- coding: utf-8 -*-
import numpy as np
import json
import re
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rc('xtick', labelsize=8)

# Notizen:
#
# -todo:
#  -Aufräumen, umbenennnen Variablen, säubern
#  -Beschriftungen in gutem Englisch
#  -git hochladen
#  -nur die max columns auswählen(top10) oder nur untersten
#  -More efficient JSON öffnen
#
# -Allgemeine Funktionen:
#  -Open data and make them ready for use
#  -Print an Instance as readeble output
#  -
#  +Visualization:
#   -Count of x in time
#   -plot x to y (with specific choices)
#
#
#
#
#
#
#
#


class FBI_data_analysis:
    """
    This project aims to analyze the FBI Crime Statistic dataset.
    This class has general functions like opening the FBI data.
    Additionaly it can generate relations between 2 (or more, in work) variables,
    Furthermore it visualizes 2 dimensional relations. 
    """

    """ General Functions """

    def __init__(self):
        self.indexes = {}
        self.fontsize_x_ticks = 7
        self.fontsize_y_ticks = 12
        self.rotation_x_axis = 90
        self.figure_size = (12,7)

        return

    def openData_JSON(self, filename):
        """
        Open the FBI crime statistics database and save all different types of each columns for further use.
        :param filename: Path to the file
        :var self.indexes , All columns and their types used in the FBI dataset
        :return: Returns the data as a JSON Object
        """
        data = json.load(open(filename))

        for inst in data['data']:
            for index in xrange(len(inst)):
                try:
                    self.indexes[index].add(inst[index])
                except KeyError:
                    try:
                        self.indexes[index] = set([inst[index]])
                    # Für index 29 was eine Liste ist und nicht sich im Set speichern lässt
                    except TypeError:
                        self.indexes[index] = tuple([inst[index]])
                        #continue
                except AttributeError:
                    continue
                    # self.indexes[index].append(inst[index])
        self.database = data
        return data

    def printinstance(self, meta, datainstance):
        """
        Prints a specific instance of the dataset in readable output.
        :param datainstance: Dictionary: The Crime Description Instance. 
        :return: 
        """

        metacolumns = meta['view']['columns']
        print metacolumns

        i = 0

        for metaid in metacolumns:
            try:
                if metaid['id'] == -1:
                    continue
                print metaid['description'].replace("\n", "") + "\t"

                if metaid['position'] > 2:

                    print datainstance[metaid['position'] + 7]
                else:
                    print datainstance[metaid['position']]
            except IndexError:
                print "IndexError. Probably a broken or wrong Data-instance: "
                print metaid
                continue

        return


    """ Data Science Functions """

    def data_relation(self, columns, data=None):
        """
        :param columns: List of all columns you want to analyse regarding the relations
        :return: Returns a [] of all relations and their counts. 
        """

        if not data:
            data = self.database['data']

        rel_matrix = {}

        print self.indexes[25]

        #brauchst gelub ich nicht über alle columsn sondern nur über das eine das über alle geht weil wir annehmen dass
        # (Arson,Street) == (Street,Arson)
        # Es soll (Arson,Street,2006)=0 sein NICHT (Arson,Street)=0, (Arson,2006)

        #für alle einzelnen crimes

        i = 0
        #Build with self.indexes all possible relations with each having 0 count

        for column_index in xrange(len(columns)):

            for columnitem1 in self.indexes[columns[column_index]]:

                i  = i + 1
                string = ""
                for column in columns[1:]:
                    string = string + "- "+ column[i] + " - "
                print string
                rel_matrix.append[string] = 0





        print columns
        #for column_index in self.indexes[columns[0]]:
        #    #für alle
        #    for column2 in xrange(len(column_index)-1):
        #        for column3 in self.indexes[column2]:
        #            rel_matrix[(column_index,column3)] = 0

        print "Rel"
        print sorted(rel_matrix.iterkeys())

        for instc in data:
            #instc = {crime:"ASSAULT",date:"2007",column:"value"}

            for column_index in columns:
                if column_index == None:
                    break

            try:
                continue

            except ValueError:
                continue

        return


    def datatable_variables2D(self, column_x, column_y):
        """
        Creates a table with 2 depending variables 
        Takes as arguments 2 columns(index of the dataset, see the indexlist in main for all indexnumbers and descriptions).
        :param column_x: The index of the column for the x axis.
        :param column_y: The index of the column for the y axis.
        ##### Example #######################
        datatable(data,13,16)
        13 = Primary description of the crime
        16 = Year it was registered
        #####################################
        Returns a map with all relations with counts.
        """
        data = self.database['data']
        #Col_y_xcount (x and y switched on purpose for later use)
        col_y_col_x_count = {}
        col_x = set()
        col_y = set()

        rel_matrix = {}

        for instance in data:
            if instance[column_x] == None or instance[column_y] == None:
                continue
            else:
                try:
                    col_y.add(instance[column_y])
                    col_x.add(instance[column_x])
                    col_y_col_x_count[(instance[column_y], instance[column_x])] = col_y_col_x_count[(instance[column_y], instance[column_x])] + 1
                except KeyError:
                    col_y_col_x_count[(instance[column_y], instance[column_x])] = 1

        col_y = sorted(col_y)
        col_x = sorted(col_x)

        columns_sorted = sorted(col_y_col_x_count.iterkeys())
        column_y_sorted = []
        for c_y in columns_sorted:
            column_y_sorted.append(c_y[1])
        column_y_sorted = sorted(column_y_sorted)


        # Find the longest String in each of the columns. This is for formatting purposes in the final tableprint.
        maxlength_col_x = ""
        for instance in col_x:
            if len(str(instance)) > len(str(maxlength_col_x)):
                maxlength_col_x = instance
        maxlength_col_y = ""
        for instance in col_y:
            if len(str(instance)) > len(str(maxlength_col_y)):
                maxlength_col_y = instance


        # print col_x
        # print len(col_y)
        # print col_y_col_x_count
        # print "listsorted"
        # print columns_sorted
        # print rel_matrix

        # (Maybe as return argument)
        self.current_x_columnlist = col_x
        self.current_y_columnlist = col_y

        index_columnsorted = 0

        # Create the relation between the columns, also creating a table to print(with printline)
        for c_y in col_y:
            lineprint = str(c_y) + str((len(str(maxlength_col_y)) - len(str(c_y)) + 1) * " ")

            for index_col_x in xrange(len(col_x)):
                try:
                    if columns_sorted[index_columnsorted][0] == c_y:
                        try:
                            if col_x[index_col_x] != columns_sorted[index_columnsorted][1]:
                                lineprint = lineprint + "0" + "\t"
                                rel_matrix[col_x[index_col_x],c_y ] = 0

                            if col_x[index_col_x] == columns_sorted[index_columnsorted][1]:
                                lineprint = lineprint + str(col_y_col_x_count[columns_sorted[index_columnsorted]]) + "\t"
                                rel_matrix[col_x[index_col_x],c_y] = col_y_col_x_count[columns_sorted[index_columnsorted]]
                                index_columnsorted = index_columnsorted + 1

                        except IndexError:
                            lineprint = lineprint + "0" + "\t"
                            rel_matrix[col_x[index_col_x],c_y] = 0
                    else:
                        lineprint = lineprint + "0" + "\t"
                        rel_matrix[col_x[index_col_x],c_y] = 0
                except IndexError:
                    lineprint = lineprint + "0" + "\t"
                    rel_matrix[col_x[index_col_x],c_y] = 0
            print lineprint

        finishprint_vertical = []

        for index_col_x in xrange(len(str(maxlength_col_x))):
            finishprint_vertical.append([])

        # Create the array for the x axis description. #####################################
        for instance in col_x:
            instance = str(instance)
            index_columnsorted = 0
            for index_col_x in xrange(len(str(maxlength_col_x))):
                try:
                    finishprint_vertical[index_col_x].append(instance[index_columnsorted])
                    index_columnsorted = index_columnsorted + 1
                except IndexError:
                    finishprint_vertical[index_col_x].append("")
                    index_columnsorted = index_columnsorted + 1
        print ""
        for instance in finishprint_vertical:
            string_x_axis = " " * (len(str(maxlength_col_y)) + 1)
            for b in instance:
                string_x_axis = string_x_axis + b + "\t"
            print string_x_axis


        return rel_matrix



    """ Visualization of data """

    ### Braucht : -plot sollten wie in age hart von zb. 2006 zu 2007 gehen
                # -muss beschrieben werden dass nur x leiste mit namen ausgegeben wird und y mit COUNTS
                # -multibarmethode? nachgucken

    #ReMOVE all specific columns that are not in rel_matrix
    #schönere Plots mit nullen dazwischen(siehe unten), Problem: x axis mit den namen benennen (column_x)
        #wie umbenennen von zahlen komplett x achse umbennen aber werte beibehalten
    def plot_x_to_y(self, columns_index, columns_x=None, columns_y=None, topn=None):
        """
        Creates a visualisation for 2 columns. 
        :param columns_index: List of required Columnindexes in the FBI dataset
        :param columns_x: The specific Objects wanted in the Columns, x axis, uses all if not given.
        :param columns_y: The specific Objects wanted in the Columns, y axis, uses all if not given.
        :param topn: Display only the the Top counted columns of y
        :return: 
        
        """

        data = self.database['data']

        if len(columns_index) != 2:
            raise Exception("Columnlist have to be size 2")

        rel_matrix = self.datatable_variables2D(columns_index[0], columns_index[1])

        if not columns_x:
            columns_x = self.current_x_columnlist
        else:
            columns_x = sorted(columns_x)
        if not columns_y:
            columns_y = self.current_y_columnlist
        else:
            columns_y = sorted(columns_y)

        print rel_matrix

        plots = []

        sorted_matrix = sorted(rel_matrix)
        print sorted_matrix

        for y in columns_y:
            print y
            ylist = []
            for x in columns_x:
                try:
                    ylist.append(rel_matrix[(x, y)])

                except KeyError:
                    ylist.append(0)
                    continue

            plots.append(ylist)


        plt.figure(figsize=self.figure_size)
        plt.xticks(rotation=self.rotation_x_axis)
        plt.tight_layout()


        if not topn:

            for plot_i in xrange(len(plots)):
                plt.scatter(sorted(columns_x), plots[plot_i])
                plt.plot(sorted(columns_x), plots[plot_i], label=columns_y[plot_i])

        else:
            values={}
            for plot_i in xrange(len(plots)):
                values[(sum(plots[plot_i]))] = plot_i

            sorted_values = sorted(values.iterkeys(), reverse=True)[:topn]

            for v in sorted_values:
                plt.scatter(sorted(columns_x), plots[values[v]])
                plt.plot(sorted(columns_x), plots[values[v]],label=columns_y[values[v]])

        print plots

        plt.tight_layout()
        plt.legend()
        plt.show()

        return

    def bar_specific_crime_to_specific_year(self, crime, min_time, max_time):
        """
        Creates a specific crime to time visualization. More detailed than plot_x_to_y with crime and time.
        :param crime: The specific crime from column index:13.
        :param min_time: The starting year you want to investigate
        :param max_time: The ending year you want to investigate
        :return: 
        """

        data = self.database['data']

        rel_matrix = self.datatable_variables2D(25, 13)
        names_times = list(str(s) for s in xrange(int(min_time), int(max_time) + 1))

        values = []

        for year in names_times:
            try:
                values.append(rel_matrix[(year, crime)])
            except KeyError:
                values.append(0)
                continue


        plt.figure("Crime over time",figsize=self.figure_size)
        plt.xticks(rotation=self.rotation_x_axis)

        plt.bar(names_times, values)
        plt.xlabel("Time in years")
        plt.ylabel("Amount of " + crime)
        plt.tight_layout()
        plt.show()

        return


if __name__ == '__main__':
    ### Meta ###
    ###

    ### File Cleaning ###
    # json split needed

    # Index 1:Unique identifier for the record.
    # C8DA5D73-201A-423C-9EAC-230CED861C25
    #
    # Index 2:The Chicago Police Department RD Number (Records Division Number), which is unique to the incident.
    # 9357606
    #
    # Index 10:Date when the incident occurred. this is sometimes a best estimate.
    # 2006-08-02T13:00:00
    #
    # Index 11:The partially redacted address where the incident occurred, placing it on the same block as the actual address.
    # 088XX S EXCHANGE AVE
    #
    # Index 12:The Illinois Unifrom Crime Reporting code. This is directly linked to the Primary Type and Description. See the list of IUCR codes at https://data.cityofchicago.org/d/c7ck-438e.
    # 1320
    #
    # Index 13:The primary description of the IUCR code.
    # CRIMINAL DAMAGE
    #
    # Index 14:The secondary description of the IUCR code, a subcategory of the primary description.
    # TO VEHICLE
    #
    # Index 15:Description of the location where the incident occurred.
    # STREET
    #
    # Index 16:Indicates whether an arrest was made.
    # False
    #
    # Index 17:Indicates whether the incident was domestic-related as defined by the Illinois Domestic Violence Act.
    # False
    #
    # Index 18:Indicates the beat where the incident occurred.  A beat is the smallest police geographic area – each beat has a dedicated police beat car.  Three to five beats make up a police sector, and three sectors make up a police district.  The Chicago Police Department has 22 police districts.  See the beats at https://data.cityofchicago.org/d/aerh-rz74.
    # 0423
    #
    # Index 19:Indicates the police district where the incident occurred.  See the districts at https://data.cityofchicago.org/d/fthy-xz3r.
    # 004
    #
    # Index 20:The ward (City Council district) where the incident occurred.  See the wards at https://data.cityofchicago.org/d/sp34-6z76.
    # 10
    #
    # Index 21:Indicates the community area where the incident occurred.  Chicago has 77 community areas. See the community areas at https://data.cityofchicago.org/d/cauq-8yn6.
    # 46
    #
    # Index 22:Indicates the crime classification as outlined in the FBI's National Incident-Based Reporting System (NIBRS).See the Chicago Police Department listing of these classifications at http://gis.chicagopolice.org/clearmap_crime_sums/crime_types.html.
    # 14
    #
    # Index 23:The x coordinate of the location where the incident occurred in State Plane Illinois East NAD 1983 projection.  This location is shifted from the actual location for partial redaction but falls on the same block.
    # 1197298
    #
    # Index 24:The y coordinate of the location where the incident occurred in State Plane Illinois East NAD 1983 projection. This location is shifted from the actual location for partial redaction but falls on the same block.
    # 1846988
    #
    # Index 25:Year the incident occurred.
    # 2006
    #
    # Index 26:Date and time the record was last updated.
    # 2016-04-15T08:55:02
    #
    # Index 27:The latitude of the location where the incident occurred. This location is shifted from the actual location for partial redaction but falls on the same block.
    # 41.734990948
    #
    # Index 28:The longitude of the location where the incident occurred. This location is shifted from the actual location for partial redaction but falls on the same block.
    # -87.552762158
    #
    # Index 29:The location where the incident occurred in a format that allows for creation of maps and other geographic operations on this data portal. This location is shifted from the actual location for partial redaction but falls on the same block.
    # [u'{"address":"","city":"","state":"","zip":""}', u'41.734990948', u'-87.552762158', None, False]

    fbi = FBI_data_analysis()
    database = fbi.openData_JSON("/media/Jung/Desktop/Arbeit & Karierre/Datenbanken zum Üben & Arbeiten/FBI Crime Statistics/xaa")
    meta = database['meta']

    ## Matplotlib Parameters

    # Roation of text of the x axis
    fbi.rotation_x_axis = 90

    # Fontsize text of the x axis
    fbi.fontsize_x_ticks = 7

    # Fontsize text of the y axis
    fbi.fontsize_y_ticks = 12

    #Size of the Figure created
    fbi.figure_size = (12, 7)


    #fbi.printinstance(meta, database['data'][0])

    # DataTable
    #fbi.datatable_variables2D(13,15)

    # Visualization
    fbi.plot_x_to_y([25, 13],topn=10)
    #fbi.plot_x_to_y([15, 13],columns_x=["GAS STATION","DRUG STORE","DAY CARE CENTER","COMMERCIAL / BUSINESS OFFICE","CLEANING STORE","PARK PROPERTY","ATM (AUTOMATIC TELLER MACHINE)","ABANDONED BUILDING","SIDEWALK","APARTMENT","YARD","STREET","BANK","CHA APARTMENT"],topn=10)
    #fbi.bar_specific_crime_to_specific_year("BATTERY","2005","2016")
    #fbi.data_relation([13,15,25])