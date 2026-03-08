import pandas as pd
import numpy as np

def curate_aimd_trajectories(input_file):
    """
    针对 NSR (2022) 论文逻辑还原的数据治理流水线。
    功能：从原始 AIMD 轨迹中筛选物理稳定态，并转化为 LDM 描述符。
    """
    # 1. 模拟读取原始数据 (例如从 OUTCAR 提取的能量和坐标)
    # df = pd.read_csv(input_file)
    print(f"Loading raw trajectories from: {input_file}")
    
    # 伪造一个演示数据集
    data = {
        'step': range(100),
        'energy': np.random.normal(-500, 2, 100),  # 总能
        'force_max': np.random.uniform(0.01, 0.5, 100), # 最大受力
        'local_density': np.random.uniform(2.5, 3.5, 100) # 局域密度
    }
    df = pd.DataFrame(data)

    # 2. 物理约束清洗 (Physics-informed Filtering)
    # 逻辑：剔除能量波动过大（未收敛）或受力异常的瞬态构型
    energy_threshold = -498.5
    force_limit = 0.3
    
    curated_df = df[
        (df['energy'] < energy_threshold) & 
        (df['force_max'] < force_limit)
    ].copy()
    
    print(f"Data Curation Complete: {len(curated_df)} stable configurations retained.")

    # 3. 特征工程 (Feature Engineering: LDM Mapping)
    # 逻辑：将物理参数映射为具备旋转不变性的描述符 (Descriptor)
    # 简化版逻辑：将局域密度归一化作为特征
    curated_df['ldm_descriptor'] = (curated_df['local_density'] - curated_df['local_density'].mean()) / curated_df['local_density'].std()

    return curated_df

if __name__ == "__main__":
    # 执行流水线
    processed_data = curate_aimd_trajectories("aimd_raw_output.log")
    print("Structured Matrix for AI Training (Top 5 rows):")
    print(processed_data[['step', 'energy', 'ldm_descriptor']].head())
