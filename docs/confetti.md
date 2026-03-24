# Confetti Explosion Animation

The SHARE Bear waitlist features a celebratory "confetti explosion" animation when a student successfully registers. This effect enhances the registration experience and reinforces the brand's welcoming and community-focused identity.

## Technical Details

- **Library:** [Canvas-confetti](https://www.npmjs.com/package/canvas-confetti) (v1.9.3) delivered via CDN.
- **Trigger Logic:** The animation is triggered automatically on the homepage (`home.html`) if either of the following conditions is met:
    1.  A success message is present in the Django `messages` framework.
    2.  The `test_success=true` query parameter is present in the URL.
- **Visuals:** 
    - **Duration:** 3 seconds of sustained "bursts".
    - **Origin:** Particles explode from both the left and right sides of the viewport (simulating a double cannon).
    - **Colors:** Custom particles using the SHARE Bear brand palette:
        - Primary Green: `#003020`
        - Container Green: `#154734`
        - Baylor Gold: `#feb71a`
        - White: `#ffffff`

## Implementation Details

The core logic is located in the `{% block extra_scripts %}` of `templates/home.html`. It uses a `setInterval` loop to create continuous bursts until the 3-second duration expires.

```javascript
// Example snippet of the trigger logic
const hasMessages = {{ messages|yesno:"true,false" }};

if (hasMessages) {
    setTimeout(triggerConfetti, 300);
}
```
