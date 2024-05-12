package medium;

public class TakingMaximumEnergyFromMysticDungeon {
    public int maximumEnergy(int[] energy, int k) {
        int result = energy[energy.length - 1];
        for (int startPoint = 0; startPoint < k; startPoint++) {
            int maxEnergy = 0;
            for (int i = startPoint; i < energy.length; i += k) {
                maxEnergy = Math.max(maxEnergy + energy[i], energy[i]);
            }
            result = Math.max(result, maxEnergy);
        }
        return result;
    }
}
