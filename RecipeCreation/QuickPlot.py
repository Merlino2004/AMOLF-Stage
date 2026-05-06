import numpy as np
import matplotlib.pyplot as plt
import mplcursors

def plottingAMU(t,Table_AMU_C1, Table_AMU_C2, ICP_AMU_C1, ICP_AMU_C2, Table_max, Table_av, ICP_max, ICP_av, run_count, ):
    # ICP plot
    plt.title(f'ICP AMU, Reflected max: {ICP_max:.2f}%, av: {ICP_av:.2f}%')
    plt.scatter(t,ICP_AMU_C1,color='blue',label='ICP_AMU_C1')
    plt.scatter(t,ICP_AMU_C2,color='red',label='ICP_AMU_C2')

    plt.grid()
    plt.xlabel('Time [s]')
    plt.ylabel('Magnetude')
    plt.legend()

    # Save and show
    plt.savefig(f'plots/Plots_RP/ICP_AMU_run{run_count}.pdf')
    plt.show()

    # Table plot
    plt.title(f'Table AMU, Reflected max: {Table_max:.2f}%, av: {Table_av:.2f}%')
    plt.scatter(t,Table_AMU_C1,color='blue',label='Table_AMU_C1')
    plt.scatter(t,Table_AMU_C2,color='red',label='Table_AMU_C2')
    plt.grid()
    plt.xlabel('Time [s]')
    plt.ylabel('Magnetude')
    plt.legend()

    # Save and show
    plt.savefig(f'plots/Plots_Mean_Real/Table_AMU_run{run_count}_mean.pdf')
    plt.show()

def AMUconverge(iteration,md_tables_c1,md_tables_c2,md_icp_c1,md_icp_c2,icp_c1, icp_c2, rf_c1, rf_c2):
    MD = [md_tables_c1,md_tables_c2,md_icp_c1,md_icp_c2]
    parameters = [icp_c1,icp_c2,rf_c1,rf_c2]
    parameters_labels = ['icp_c1','icp_c2','rf_c1','rf_c2']
    colors = ['r','b','g','y']
    scatters = []

    for i in range(len(parameters)):
        plt.plot(iteration,parameters[i],color=colors[i])
        scatter = plt.scatter(iteration,parameters[i], label=parameters_labels[i],color=colors[i])
        scatters.append(scatter) 

        cursor = mplcursors.cursor(scatters, hover=True)
        @cursor.connect("add")
        def on_add(sel):
            i = scatters.index(sel.artist)
            j = sel.index
            sel.annotation.set_text(f"Mean Deviation: {MD[i][j]:.2f}")

    plt.grid()
    plt.xlabel('Iterations')
    plt.ylabel('Positions (%)')
    plt.legend()

    plt.savefig(f'plots/Plots_Mean_Real/Conclusions/ConvergePlot_MeanDeviation.pdf')
    plt.show()

def PlotReflected(iteration,reflected_table,reflected_icp):
    reflected = [reflected_table,reflected_icp]
    reflected_labels = ['reflected_table','reflected_icp']
    colors = ['r','b']

    for i in range(len(reflected)):
        plt.plot(iteration,reflected[i],color=colors[i])
        plt.scatter(iteration,reflected[i],label=reflected_labels[i],color=colors[i])

    plt.grid()
    plt.xlabel('Iterations')
    plt.ylabel('Reflected Percentage (%)')
    plt.legend()

    plt.savefig(f'plots/Plots_Mean_Real/Conclusions/Reflected_Iterations.pdf')
    plt.show()

def PercentageOverMD(reflected_table,reflected_icp,md_tables_c1,md_tables_c2,md_icp_c1,md_icp_c2):
    reflected = [reflected_table,reflected_icp]
    md = [(md_tables_c1+md_tables_c2)/2,(md_icp_c1+md_icp_c2)/2]
    reflected_labels = ['reflected_table','reflected_icp']
    colors = ['r','b']

    for i in range(len(reflected)):
        plt.scatter(md[i],reflected[i],label=reflected_labels[i],color=colors[i])

    plt.grid()
    plt.xlabel('Mean Deviation')
    plt.ylabel('Reflected Percentage (%)')
    plt.legend()

    plt.savefig(f'plots/Plots_Mean_Real/Conclusions/Reflected_MD.pdf')
    plt.show()

def ReflectedPoweroverC1C2(ICP_C1_Position,ICP_C2_Position,Table_C1_Position,Table_C2_Position,ICP_av,ICP_max,Table_av,Table_max):
    plt.scatter(ICP_C1_Position,ICP_av,label='ICP_C1_Position',color='r')
    plt.scatter(ICP_C2_Position,ICP_av,label='ICP_C2_Postion',color='b')
    
    plt.grid()
    plt.legend()
    plt.xlabel('Position (%)')
    plt.ylabel('Reflected Percentage (%)')

    plt.savefig(f'plots/StabilizationOptimize/ICP_ReflectedPower')
    plt.show()

    plt.scatter(Table_C1_Position,Table_av,label='ICP_C1_Position',color='r')
    plt.scatter(Table_C2_Position,Table_av,label='ICP_C2_Postion',color='b')
    
    plt.grid()
    plt.legend()
    plt.xlabel('Position (%)')
    plt.ylabel('Reflected Percentage (%)')

    plt.savefig(f'plots/StabilizationOptimize/Table_ReflectedPower')
    plt.show()