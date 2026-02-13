# AGENTS.md

This file contains guidelines and commands for agentic coding agents working in this Flutter repository.

## Project Structure

This is a Flutter project (CSM-Model) following standard Flutter architecture patterns.

## Build, Lint, and Test Commands

### Development Commands
```bash
# Get dependencies
flutter pub get

# Run the app in development mode
flutter run

# Run with specific device
flutter run -d chrome
flutter run -d macos
flutter run -d android

# Hot reload (when app is running)
press 'r' in terminal
```

### Build Commands
```bash
# Build for different platforms
flutter build apk                    # Android APK
flutter build appbundle              # Android App Bundle
flutter build ios                    # iOS
flutter build web                    # Web
flutter build macos                  # macOS
flutter build windows                # Windows
flutter build linux                  # Linux

# Build with different modes
flutter build apk --release          # Release build
flutter build apk --debug           # Debug build
flutter build apk --profile         # Profile build
```

### Testing Commands
```bash
# Run all tests
flutter test

# Run specific test file
flutter test test/widget_test.dart

# Run tests with coverage
flutter test --coverage

# Run tests in watch mode
flutter test --watch

# Run specific test case
flutter test --name "specific test name"

# Run tests for specific file pattern
flutter test test/unit/
```

### Code Quality Commands
```bash
# Analyze code for issues
flutter analyze

# Fix formatting issues
dart format .

# Fix import organization
dart fix --apply

# Run all quality checks together
flutter analyze && dart format . && flutter test
```

## Code Style Guidelines

### Import Organization
```dart
// 1. Dart imports
import 'dart:async';
import 'dart:convert';

// 2. Flutter imports
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

// 3. Package imports (alphabetical)
import 'package:http/http.dart' as http;
import 'package:provider/provider.dart';

// 4. Project imports (relative, alphabetical)
import '../models/user.dart';
import '../services/api_service.dart';
import '../widgets/custom_button.dart';
```

### File and Directory Structure
```
lib/
├── main.dart
├── app.dart
├── core/
│   ├── constants/
│   ├── errors/
│   ├── utils/
│   └── themes/
├── data/
│   ├── models/
│   ├── repositories/
│   └── services/
├── domain/
│   ├── entities/
│   ├── repositories/
│   └── usecases/
├── presentation/
│   ├── pages/
│   ├── widgets/
│   └── providers/
└── tests/
    ├── unit/
    ├── widget/
    └── integration/
```

### Naming Conventions
- **Files**: snake_case (e.g., `user_service.dart`, `custom_button.dart`)
- **Classes**: PascalCase (e.g., `UserService`, `CustomButton`)
- **Variables & Methods**: camelCase (e.g., `userName`, `getUserData()`)
- **Constants**: UPPER_SNAKE_CASE (e.g., `API_BASE_URL`, `MAX_RETRY_COUNT`)
- **Private members**: prefix with `_` (e.g., `_privateMethod`, `_internalState`)

### Dart/Flutter Specific Guidelines

#### Widget Structure
```dart
class CustomWidget extends StatelessWidget {
  const CustomWidget({
    super.key,
    required this.title,
    this.onTap,
  });

  final String title;
  final VoidCallback? onTap;

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onTap,
      child: Container(
        // Widget implementation
      ),
    );
  }
}
```

#### State Management
- Use Provider or Riverpod for state management
- Keep business logic out of UI widgets
- Use repository pattern for data layer

#### Error Handling
```dart
// Use try-catch with specific exception types
try {
  final result = await apiService.getData();
  return result;
} on SocketException {
  throw NetworkException('No internet connection');
} on TimeoutException {
  throw NetworkException('Request timeout');
} catch (e) {
  throw UnknownException('Unexpected error: $e');
}
```

#### Async Programming
- Always use `async`/`await` instead of `.then()`
- Handle loading and error states properly
- Use `FutureBuilder` or `StreamBuilder` for async UI

### Testing Guidelines
- Write unit tests for business logic
- Write widget tests for UI components
- Use descriptive test names
- Mock external dependencies using `mockito`

### Code Formatting
- Use `dart format` for consistent formatting
- Maximum line length: 80 characters
- Use trailing commas for multi-line parameters/lists
- Add proper documentation comments (`///`) for public APIs

### Git Conventions
- Use conventional commits: `feat:`, `fix:`, `refactor:`, `test:`, etc.
- Keep commits small and focused
- Write clear, descriptive commit messages

### Performance Guidelines
- Use `const` constructors where possible
- Optimize widget rebuilds with `const` and proper keys
- Use `ListView.builder` for long lists
- Implement proper image caching

### Security Guidelines
- Never commit API keys or secrets
- Use environment variables for sensitive data
- Validate user inputs properly
- Use HTTPS for network requests