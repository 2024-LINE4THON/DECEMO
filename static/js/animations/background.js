class BackgroundAnimation {
    constructor(options = {}) {
        this.snowflakeCount = options.snowflakeCount || 10000;
        this.init();
    }

    init() {
        this.initSnow();
    }

    initSnow() {
        const snowContainer = document.getElementById('snow');
        if (!snowContainer) return;

        for (let i = 0; i < this.snowflakeCount; i++) {
            const flake = document.createElement('div');
            flake.className = 'flake';
            snowContainer.appendChild(flake);
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new BackgroundAnimation({
        snowflakeCount: 10000
    });
});